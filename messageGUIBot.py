#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:12:12 2019

@author: alexrandall
"""

#message bot

import pyautogui, time


message = input('Spam your friends! Type you message: ')

time.sleep(3)

pyautogui.click((312, 666))

i = 101
while i>0:
    pyautogui.typewrite(message)
    pyautogui.typewrite('\n')
    i -= 1

#here comes 100 text messages guys