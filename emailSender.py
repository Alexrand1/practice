#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:14:07 2019

@author: alexrandall
"""

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def emailSender(email, message, subject):
    browser = webdriver.Firefox(executable_path=r'/Users/alexrandall/Documents/geckodriver')
    browser.implicitly_wait(10)
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys('alex.w.randall@gmail.com')
    nextElem = browser.find_element_by_id('identifierNext')
    nextElem.click()
    wait = WebDriverWait(browser, 1500)
    passwordElem = browser.find_element_by_name("password")
    time.sleep(5)
    passwordElem.send_keys('Vertigo1')
    pnextElem = browser.find_element_by_id('passwordNext')
    pnextElem.click()    
    
    time.sleep(4)
    composeElem = browser.find_element_by_class_name('T-I.J-J5-Ji.T-I-KE.L3').click()
    
    toElem = browser.find_element_by_id(':ok')
    time.sleep(3)
    toElem.send_keys(email)
    subElem = browser.find_element_by_id(':o2')
    subElem.send_keys(subject)
    time.sleep(1)
    
    bodyElem = browser.find_element_by_id(':p7')
    bodyElem.send_keys(message)
    time.sleep(1)
    
    sendElem = browser.find_element_by_id(':ns')
    sendElem.click()
    
if __name__ == '__main__':
    email = input('Enter the email address you would like to send a message too: ')
    subject = input('enter your email subject: ')
    message = input('Input your message body here: ')
    
    emailSender(email, message, subject)
    
    




