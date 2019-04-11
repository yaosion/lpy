import itchat
import requests
import json

def get_response(msg):
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # userid = int(time.time())
    data = {
        "perception": {
            "inputText": {
                "text": msg
            }
        },
        "userInfo": {
            "apiKey": "6432af772fb641da95d79ef02fa5a2ca1", #图灵机器人apikey
            "userId": 'cba1a2bd794e513b', #随意字符串，但是图灵默认一个字符串为一个用户
        }
    }
    jsondata = json.dumps(data)
    response = requests.post(api, data=jsondata)
    print(response)
    robot_res = json.loads(response.content)
    print(robot_res["results"][0]['values']['text'])
    return robot_res["results"][0]['values']['text']
@itchat.msg_register(itchat.content.TEXT) # 用于接收来自朋友间的对话消息
def print_content(msg):
    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True) # 用于接收群里面的对话消息
def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(hotReload=True) # 通过微信扫描二维码登录
itchat.run()


