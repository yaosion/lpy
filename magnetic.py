# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:25:45 2019
@author: ay

"""

import requests
from bs4 import BeautifulSoup


# 获取当前页HTML内容
def getHTML(url,headers):
    try:
        r=requests.post(headers+url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return False

# 爬取当前页搜索结果内的url
def getUrl(html):
    urlList = []
    soup=BeautifulSoup(html,'html.parser')
    for u in soup.find_all('div',class_='item-title'):
        t=u.find('a')
        urlList.append(t['href'])
    return urlList

# 爬取单条页下的磁力链
def getMagnetic(html):
    magneticList = []
    soup=BeautifulSoup(html,'html.parser')
    for u in soup.find_all('div',class_='panel-body'):
        t=u.find('a')
        if t != None:
            magneticList.append(t.text)
    return magneticList

# 获取输入内容，调用请求，返回请求数据
def getInput(strs,page):
    setStr = strs or '能输入内容？'
    setpage = page or '1'
    print('------输入的内容-----'+setStr)
    print('------页------码-----'+setpage)
    html = getHTML('/search/'+setStr+'/default-'+setpage+'.html','https://btcat.bid')
    return html

# 主函数
def main():
    htmlText = getInput('明日花','1')
    if htmlText:
        urlList = getUrl(htmlText)
        n = len(urlList)
        while n>=0:
            magHtml = getHTML(urlList[n-1],'https://btcat.bid')
            magneticList = getMagnetic(magHtml)
            print('-----------返回磁力----------')
            for i in range(1,3):
                print(magneticList[i-1])
            n = n-1

# 防模块自调用
if __name__=='__main__':
    main()  