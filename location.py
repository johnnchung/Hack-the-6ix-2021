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
pyautogui.FAILSAFE = False

from iteration_utilities import duplicates

class Link_Class:
    def __init__(self, left_top_corner, right_bottom_corner, left_bottom_corner, right_top_corner): 
        self.left_top = left_top_corner
        self.right_bottom = right_bottom_corner
        self.left_bottom = left_bottom_corner
        self.right_top = right_top_corner
        
    
def find_location(url, bad_links): 
        
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    minimumWindow = False

    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    browser.get(url)
    
    browser.maximize_window()
    
    # if minimumWindow:
    #     pyautogui.moveTo(600, 3, 1)
    #     pyautogui.dragTo(0, 200, 1, button='left')
    
    link_coordinate_array = [] 

    for link in bad_links: 
        try: 
            e = browser.find_element_by_xpath('//a[@href="'+link+'"]') 
            print(link)

            location = e.location #size for default 1920/1080 screen
            size = e.size
            height = size['height']
            width = size['width']
        
        except: 
            continue

        #a = browser.execute_script("return outerWidth")
        #c = browser.execute_script("return outerHeight - innerHeight")
        #b = browser.execute_script("return outerHeight")
        a = 1920
        b = 1040
        c = 115
        pyautogui.moveTo(location['x']*1920/a, (location['y'] + c)*1080/b, 0.1)
        pyautogui.moveTo(location['x']*1920/a, (location['y'] + c)*1080/b, 0.1) #account for user screen size

        (x, y) = (round(location['x']*1920/a), round((location['y'] + c)*1080/b)) # or floor
        #x = x - 1
        y = y - 10
        
        left_top_corner = (x, y)
        right_bottom_corner = (x + width, y + height)
        left_bottom_corner = (x, y + height)
        right_top_corner = (x + width, y)

        #pyautogui.moveTo(x, y, 0.5)
        #pyautogui.moveTo(x, y + height, 0.5)
        #pyautogui.moveTo(x + width, y + height, 0.5)
        #pyautogui.moveTo(x + width, y, 0.5)
            
        link_object = Link_Class(left_top_corner, right_bottom_corner, left_bottom_corner, right_top_corner)
        
        link_coordinate_array.append(link_object)
        print(link_object.left_top, link_object.right_top, link_object.left_bottom, link_object.right_bottom)

    return link_coordinate_array