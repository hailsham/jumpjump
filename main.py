# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:03:48 2017

@author: Leifei
"""

import os
from tiao import get_dist, dist2time
import time


def jump(time):
    cmd = 'adb shell input swipe 50 250 250 250 {}'.format(int(time*1000))
    os.popen(cmd)
    
def get_screen():
    os.system('adb shell screencap -p /sdcard/1.png')
    os.system('adb pull /sdcard/1.png .')

    
def main():
    while True:
        get_screen()
        dist,img = get_dist()
        t = dist2time(dist)
        print t
        jump(t)
        time.sleep(1)

if __name__ == '__main__':
    main()
