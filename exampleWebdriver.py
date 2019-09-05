#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:01:23 2019

@author: alexrandall
"""

from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'/Users/alexrandall/Documents/geckodriver')
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_elem_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that tag name')
    