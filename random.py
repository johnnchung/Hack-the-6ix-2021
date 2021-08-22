from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import datetime

import pyautogui
import os
from collections import OrderedDict
import urllib.request
from pathlib import Path
from requests import get
import time

def find_location(bad_links): 
        
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    minimumWindow = False

    # def internet_on():
    #     i = 0
    #     while True:
    #         try:
    #             urllib.request.urlopen('http://www.google.com', timeout=20)
    #             return True
    #         except:
    #             print("Internet not found for last %s minutes" % i)
    #             i = i + 1
    #             time.sleep(60)
    #             pass

    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    browser.maximize_window()

    if minimumWindow:
        pyautogui.moveTo(600, 3, 1)
        pyautogui.dragTo(0, 200, 1, button='left')
        
    browser.get('https://en.wikipedia.org/wiki/Main_Page')
    # print(browser.getCurrentUrl())
    link = '/wiki/The_40-Year-Old_Virgin' 

    e = browser.find_element_by_xpath('//a[@href="'+link+'"]') 

    location = e.location #size for default 1920/1080 screen
    size = e.size

    print(location)
    print(size)

    a = browser.execute_script("return outerWidth")
    b = browser.execute_script("return outerHeight")
    c = browser.execute_script("return outerHeight - innerHeight")
    print(a,b,c)
    pyautogui.moveTo(location['x']*1920/a, (location['y'] + c)*1080/b, 0.1) #account for user screen size

    (x, y) = pyautogui.position()
    (height, width) = (size['height']*1920/a, (size['width'] + c)*1080/b)
    left_bottom_corner = (x, y)
    right_bottom_corner = (x + width, y)
    left_top_corner = (x, y - height)
    right_top_corner = (x + width, y - height)

    print(str(left_bottom_corner) + " " + str(right_bottom_corner) + " " + str(right_bottom_corner) + " " +str(right_bottom_corner))