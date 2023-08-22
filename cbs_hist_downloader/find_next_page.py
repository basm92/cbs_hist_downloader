#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:34:30 2023

@author: baswork
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

def find_next_page(driver, con_tinue):
    
    elements = driver.find_elements(By.CSS_SELECTOR, '#collection-navigation > div > a, #collection-navigation > div > span')
    # Iterate through the elements to find the one with aria-current="true"
    current_element = None
    for element in elements:
        aria_current = element.get_attribute('aria-current')
        if aria_current == 'true':
            current_element = element
            break
    # Find where we are in the list of elements 
    current_index = elements.index(current_element)
    
    # Find the next element if there is any
    if current_index < len(elements) - 3:
        next_element = elements[current_index + 1]
        # Click the next element if it had been found
        next_element.click()
    else:
        # Otherwise terminate the loop
        con_tinue = False
        print("No next element found.")
        driver.quit()
    return con_tinue
