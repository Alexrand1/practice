#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:12:04 2019

@author: alexrandall
"""

import pyautogui

print('Press CTRL-C to quit')
try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        ç
except KeyboardInterrupt:
    print('\nDone')
    
    

