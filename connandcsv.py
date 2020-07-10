# ！/usr/bin/env/python
# -*- coding:utf-8 -*-
import configparser
import csv
import datetime
import os
import shutil
import pymssql
import decimal
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_UI import *  # 导入我们刚转换的ui

decimal.__version__


# 连接函数
def connDb(_ip, _name, _pwd, _db, t):
    # 连接数据库
    conn = pymssql.connect(_ip, _name, _pwd, _db)
    if conn:
        print("连接成功!")
    else:
        print("连接失败")
        conn.close()
        return
    # 打开数据库连接池
    cursor = conn.cursor()

    # 检查是否有execText.txt，执行存储过程
    # if not os.path.exists("./execText.txt"):
    #     with open('./execText.txt', "w", encoding='UTF-8') as t:
    #         t.close()
    # 打开execText文件
    # with open('./execText.txt', "r", encoding='UTF-8') as execRead:
    #     execReadData = execRead.read()  # 读取文件
    # 检查是否有sqlText.txt，执行sql过程
    if not os.path.exists("./sqlText.txt"):
        with open('./sqlText.txt', "w", encoding='UTF-8') as w:
            w.close()
    # 打开sqlText文件
    with open('./sqlText.txt', "r", encoding='UTF-8') as sqlRead:
        sqlReadData = sqlRead.read()  # 读取文件
    try:
        print("执行查询语句...")
        # 执行sql命令
        if len(t) > 0:
            cursor.execute(t)
        if len(sqlReadData) > 0:
            cursor.execute(sqlReadData)
        else:
            return 1
        # 读取数据
        row = cursor.fetchall()
        # 读取列属性
        cols = cursor.description
        # 列名分割
        col = []
        for i in cols:
            col.append(i[0])
        return row, col
        # 关闭连接池
        cursor.close()
        conn.close()
        sqlRead.close()
        print("获取数据结束，关闭连接池")
    except BaseException as e:
        print(e)
        # 关闭连接池
        cursor.close()
        conn.close()
        sqlRead.close()
        print("查询失败，检查sql语句")


# 获取连接配置
def getConn():
    # 读写配置文件，当配置文件不存在或者配置文件里没有对应的DB配置时自动创建
    config = configparser.ConfigParser()
    config.read("./conn.ini")
    if not os.path.exists("./conn.ini") or bool(1 - config.has_section('db')):
        with open('./conn.ini', "w", encoding='UTF-8') as f:
            config["db"] = {'ip': '',
                            'name': '',
                            'pwd': '',
                            'dbname': ''}
            config.write(f)
        f.close()
    ip = config.get('db', 'ip')
    name = config.get('db', 'name')
    pwd = config.get('db', 'pwd')
    db = config.get('db', 'dbname')
    return ip, name, pwd, db


# 写入CSV并备份
def writeCSV(s, n):
    _col = s[1]
    _row = s[0]
    if len(n) > 0:
        file_path = "./"+n+".csv"
    else:
        file_path = "./test.csv"
    with open(file_path, 'w', newline='', encoding='UTF-8') as csvObj:
        writer = csv.writer(csvObj)
        print("数据写入中...")
        # 输入列头
        writer.writerow(_col)
        # 循环写入表数据
        for item in _row:
            writer.writerow(item)
    csvObj.close()
    print("写入完成，文件位置存放于", file_path)
    time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    backup_file_path = "./Backup/" + time + ".csv"
    try:
        shutil.copy(file_path, backup_file_path)
        print("备份完成，文件位置存放于", backup_file_path)
    except IOError:
        os.mkdir('Backup')
        shutil.copy(file_path, backup_file_path)
        print("备份完成，文件位置存放于", backup_file_path)
    except BaseException as ex:
        print(ex)


# 获取时间对txt写入操作
def writeExec(s, e):
    _start = s
    _end = e
    # 检查是否有execText.txt，执行存储过程
    if not os.path.exists("./execText.txt"):
        with open('./execText.txt', "w", encoding='UTF-8') as t:
            t.close()
    # 打开execText文件
    with open('./execText.txt', "r", encoding='UTF-8') as execRead:
        execReadData = execRead.read()  # 读取文件
        if execReadData.find('start') > 0 and execReadData.find('end') > 0:
            fTime = execReadData.replace('start', _start)
            cTime = fTime.replace('end', _end)
        else:
            cTime = ''
    execRead.close()
    return cTime


# UI窗口类
class MyWindows(Ui_execSQL, QMainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)
        self.startDate.setDate(QDate.currentDate())
        self.startDate.setMaximumDate(QDate.currentDate().addDays(365))
        self.startDate.setCalendarPopup(True)
        self.startDate.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.endDate.setDate(QDate.currentDate())
        self.endDate.setMaximumDate(QDate.currentDate().addDays(365))
        self.endDate.setCalendarPopup(True)
        self.endDate.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.pushButton.clicked.connect(self.on_button_clicked)
        self.lineText.setPlaceholderText("如不输入文件名，则生成名为'test'的文件，不影响备份")

    # 定义一个输出函数
    def printf(self, mypstr):
        self.textPrint.append(mypstr)  # 在指定的区域显示提示信息
        self.cursor = self.textPrint.textCursor()
        self.textPrint.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def on_button_clicked(self):
        sStartDate = self.startDate.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        sEndDate = self.endDate.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        sName = self.lineText.text()
        self.printf("查询时间为："+sStartDate+"到"+sEndDate)
        config = getConn()
        if config[0] == '' or config[1] == '' or config[2] == '' or config[3] == '':
            self.printf('【检测到文件"conn.ini"没有配置，请配置后重新查询】')
            return
            # os.system('pause')
        else:
            self.printf('执行查询...')
            t = writeExec(sStartDate, sEndDate)
            if len(t) <= 0:
                self.printf('【检测到execText.txt为空或者没有按照要求改格式，将只执行sqlText.txt】')
            s = connDb(config[0], config[1], config[2], config[3], t)
            if s == 1:
                self.printf('【检测到两个文档均没有配置，取消查询】')
                return
            self.printf('查询结束，正在写入文档...')
            writeCSV(s, sName)
            self.printf('写入完成。')
            # os.system('pause')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_windows = MyWindows()
    my_windows.show()
    sys.exit(app.exec_())

