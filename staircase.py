#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:22:09 2019

@author: alexrandall
"""

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(n+1):
        if i == 1:
            pass
        else: 
            print(('#' * i).rjust(n))
             
    
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)