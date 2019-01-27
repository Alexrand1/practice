#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:59:20 2019

@author: alexrandall
"""

# selective copy, will copy files of only a certain type
import os, shutil


selectcopy = os.mkdir('PythonFilesFound')

for folders, subfolders, filenames in os.walk('/Users/alexrandall/Documents'):
    for filename in filenames:
        if filename.endswith('.py'):
            print(filename)
            shutil.move(filename, 'PythonFilesFound')
            
