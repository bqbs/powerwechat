#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'bat'

import itchat
from itchat.content import *


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    pass


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply_group(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg['ToUserName'] == u'filehelper':
        itchat.send('%s: %s' % (msg['Type'], msg['Text']))
    else:
        itchat.send('%s from %s' % (msg['Type'], msg['']))


def main():
    itchat.auto_login()
    itchat.run()
    itchat.dump_login_status()


if __name__ == '__main__':
    main()
