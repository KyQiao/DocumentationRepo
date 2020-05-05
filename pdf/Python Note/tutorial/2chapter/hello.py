#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test module'

__author__ ='Kaiyao Qiao'

import sys

def test():
    args = sys.argv
    if len(args) is 1:
        print('Hello, world')
    elif len(args) is 2:
        print('Hello, %s!'% args[1])
    else:
        print('Too many words.')


if __name__ == '__main__':
    test()
    