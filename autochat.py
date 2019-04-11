#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itchat
import urllib.request
from bs4 import BeautifulSoup
from magnetic import runMag
import time

# 微信发送消息
def sendMessage():
    try:
        theMag = runMag('rct','1')
    except:
        return False
    
    itchat.auto_login(hotReload=True)
    users = itchat.search_friends(name = '小明')
    
    userName = users[0]['UserName']
    ret = itchat.send(msg=theMag,toUserName = userName)

    if ret:
        print("Succeed Sending")
    else:
        print("Error sending")
    
    time.sleep(60)
    itchat.logout()

    return theMag


if __name__ == "__main__":
        text = sendMessage()
        print(text)