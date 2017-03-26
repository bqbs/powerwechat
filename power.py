#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'bat'

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    pass


def main():
    itchat.auto_login()


if __name__ == '__main__':
    main()
