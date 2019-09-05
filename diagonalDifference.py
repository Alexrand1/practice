#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:40:02 2019

@author: alexrandall
"""

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    ldiag = 0
    rdiag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                print(i)
                print(j)
                ldiag = ldiag + arr[i][j]
    for row in range(len(arr)):
        col = len(arr)- row - 1
        rdiag = rdiag + (arr[row][col])
    result = abs(ldiag - rdiag)
    return result

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
