#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Lian'

import os
# 通过该命令安装该API： pip install NetEaseMusicApi
from NetEaseMusicApi import interact_select_song

HELP_MSG = u'''\
欢迎使用微信网易云音乐
帮助： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐\
'''

with open('stop.mp3', 'w') as f: pass


def close_music():
    os.startfile('stop.mp3')


def music_player(msg):
    print(u'music player')
    if msg == u'close music':
        close_music()
        return u'音乐已关闭'
    if msg == u'music help':
        return HELP_MSG
    else:
        msg = msg.replace(u'music ', u'')
        return interact_select_song(msg)
