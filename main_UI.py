# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_execSQL(object):
    def setupUi(self, execSQL):
        execSQL.setObjectName("execSQL")
        execSQL.resize(500, 500)
        execSQL.setMinimumSize(QtCore.QSize(500, 500))
        execSQL.setMaximumSize(QtCore.QSize(500, 500))
        self.pushButton = QtWidgets.QPushButton(execSQL)
        self.pushButton.setGeometry(QtCore.QRect(390, 10, 101, 61))
        self.pushButton.setObjectName("pushButton")
        self.textPrint = QtWidgets.QTextEdit(execSQL)
        self.textPrint.setGeometry(QtCore.QRect(10, 80, 481, 401))
        self.textPrint.setObjectName("textPrint")
        self.label_3 = QtWidgets.QLabel(execSQL)
        self.label_3.setGeometry(QtCore.QRect(410, 480, 81, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(execSQL)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 182, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.startDate = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.startDate.setObjectName("startDate")
        self.horizontalLayout.addWidget(self.startDate)
        self.layoutWidget1 = QtWidgets.QWidget(execSQL)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 10, 182, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.endDate = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        self.endDate.setObjectName("endDate")
        self.horizontalLayout_2.addWidget(self.endDate)
        self.label_4 = QtWidgets.QLabel(execSQL)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 36, 16))
        self.label_4.setObjectName("label_4")
        self.lineText = QtWidgets.QLineEdit(execSQL)
        self.lineText.setGeometry(QtCore.QRect(62, 50, 321, 20))
        self.lineText.setObjectName("lineText")

        self.retranslateUi(execSQL)
        QtCore.QMetaObject.connectSlotsByName(execSQL)

    def retranslateUi(self, execSQL):
        _translate = QtCore.QCoreApplication.translate
        execSQL.setWindowTitle(_translate("execSQL", "SQL执行生成CSV工具 --寮医"))
        self.pushButton.setText(_translate("execSQL", "开始"))
        self.label_3.setText(_translate("execSQL", "20200709 Hgz"))
        self.label.setText(_translate("execSQL", "开始时间"))
        self.label_2.setText(_translate("execSQL", "结束时间"))
        self.label_4.setText(_translate("execSQL", "文件名"))
