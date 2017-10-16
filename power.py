# coding=utf8
# !/usr/bin/python


__author__ = 'bat'

import itchat
from itchat.content import *
import batman

import Tuling
import music
import json

config = None
isLife = True
reply = None


def init():
    global isLife
    global reply
    load_json()
    if config is not None:
        isLife = config['autoreply']
        reply = config['reply']


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    pass


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply_group(msg):
    if msg['isAt']:
        batman.calling_batman()
        if isLife:
            reply = Tuling.get_response(msg['Content'])
            itchat.send(reply + u'(来自图灵机器人)' or u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']),
                        msg['FromUserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    global isLife
    global reply
    if msg['ToUserName'] == u'filehelper':
        if u'on' in msg['Text']:
            isLife = True
            config['autoreply'] = True
            itchat.send(u'打开自动回复', u'filehelper')
        elif u'off' in msg['Text']:
            batman.stop_calling_batman()
            isLife = True
            config['autoreply'] = False
            itchat.send(u'关闭自动回复', u'filehelper')
        elif u'music' in msg['Text']:
            text = music.music_player(msg['Text'])
            itchat.send(text, u'filehelper')
        elif u'reply' in msg['Text']:
            l = msg['Text'].split(' ')
            if len(l) >= 2:
                reply = l[1]
            else:
                # todo
                pass
    else:
        batman.calling_batman()
        if isLife:
            if reply:
                text = reply
            else:
                text = Tuling.get_response(msg['Text'])
            text += u'--来自自动回复机器人'
            itchat.send(text, msg['FromUserName'])


def load_json():
    global config
    with open('config.json', 'r') as f:
        config = json.load(f)


def dump_json():
    global config
    with open('config.json', 'w') as f:
        json.dump(config, f)


def main():
    init()

    itchat.auto_login(hotReload=True)
    itchat.run()
    itchat.dump_login_status()


if __name__ == '__main__':
    main()
