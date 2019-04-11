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
        queryUrl = headers+url
        r=requests.get(queryUrl)
        r.encoding=r.apparent_encoding
        return r.text
    except requests.exceptions.HTTPError as h:
        print(h)
        return False
    except requests.exceptions.Timeout as t:
        print(t)
        return False
    except requests.exceptions.SSLError as s:
        print(s)
        return False

# 爬取当前页搜索结果内的url
def getUrl(html):
    urlList = []
    soup=BeautifulSoup(html,'html.parser')
    for u in soup.find_all('div',class_='Search__result___2S94i'):
        t=u.find('a')
        urlList.append(t['href'])
    return urlList

# 爬取单条页下的磁力链
def getMagnetic(html):
    magneticList = []
    soup=BeautifulSoup(html,'html.parser')
    for u in soup.find_all('div',class_='Information__content_information___1e4H7'):
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
    html = getHTML('/search?word='+setStr+'&page='+setpage,'https://www.cilimao.cc')
    return html

# 磁力爬取主函数
def runMag(str,page):
    htmlText = getInput(str,page)
    theValue = []
    if htmlText:
        urlList = getUrl(htmlText)
        print('-----------返回磁力----------')
        for one in urlList:
            if 'https://pan.baidu.com' in one:
                continue
            magHtml = getHTML(one,'https://www.cilimao.cc')
            magneticList = getMagnetic(magHtml)
            theValue.append(magneticList[0])
        value = '------'.join(theValue)
        return value

# 主函数
def main():
    s = runMag('rct','1')
    print(s)

# 防模块自调用
if __name__=='__main__':
    main()  