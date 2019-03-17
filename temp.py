import itchat
import time, re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('year', msg['Text']).span()
    if(match):
        itchat.send(('Happy new year'),msg['FromUserName'])

    print(msg.FromUserName)

itchat.auto_login(enableCmdQR=2)
itchat.run(True)