#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:24:50 2019

@author: alexrandall
"""

import pyautogui, time

time.sleep(5)
pyautogui.click()
distance = 100
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.001)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.001)
    pyautogui.dragRel(-distance, 0, duration=0.001)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.001)    