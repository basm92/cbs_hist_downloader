# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from .find_next_page import find_next_page

def scrape_book(start_url):
    
    if "historisch.cbs.nl" not in start_url:
        raise ValueError("Please insert a CBS historisch link")
    
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Open the initial URL
    driver.get(start_url)

    image_element = driver.find_element(By.CSS_SELECTOR,'a.cb-enable')
    image_element.click()

    con_tinue = True
    # Main loop to navigate through pages
    while con_tinue:
        cur_url = driver.current_url
        try: 
            # Find the frame
            frames = driver.find_elements(By.CSS_SELECTOR,'iframe')
            driver.switch_to.frame(frames[0])
            
            # Locate the image element
            step1 = driver.find_element(By.CSS_SELECTOR, 'a#downloadDirect')
            step1.click()
            
            # Just leave the default resolution and click download
            step2 = driver.find_element(By.CSS_SELECTOR, 'a#downloadResLink')
            step2.click()
            
            # Locate and click the 'next' link
            driver.switch_to.default_content()
            # Draft: change the next code to be robust
            con_tinue = find_next_page(driver, con_tinue)

            # Add a short delay to ensure the page loads completely before proceeding
            time.sleep(2)  # You can adjust this delay as needed
        except:
            print("An error occurred with the Selenium package. Starting again from", cur_url)
            driver.quit()
            scrape_book(cur_url)
            
