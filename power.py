#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'bat'

import itchat
from itchat.content import *

import Tuling
import music

isDebug = True
isLife = True


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    pass


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply_group(msg):
    if msg['isAt']:
        if isLife:
            reply = Tuling.get_response(msg['Content'])
            itchat.send(reply + u'(来自图灵机器人)' or u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']),
                        msg['FromUserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    global isLife
    if msg['ToUserName'] == u'filehelper':
        if u'on' in msg['Text']:
            isLife = True
            itchat.send(u'打开自动回复', u'filehelper')
        elif u'off' in msg['Text']:
            isLife = False
            itchat.send(u'关闭自动回复', u'filehelper')
        elif u'music' in msg['Text']:
            reply = music.music_player(msg['Text'])
            itchat.send(reply, u'filehelper')
    else:
        if isLife:
            reply = Tuling.get_response(msg['Text'])
            # print(reply)
            itchat.send(reply + u'(来自图灵机器人)' or u'我的主人不在(来自自动回复机器人)', msg['FromUserName'])


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()
    itchat.dump_login_status()


if __name__ == '__main__':
    main()
