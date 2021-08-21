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

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

minimumWindow = False

def internet_on():
    i = 0
    while True:
        try:
            urllib.request.urlopen('http://www.google.com', timeout=20)
            return True
        except:
            print("Internet not found for last %s minutes" % i)
            i = i + 1
            time.sleep(60)
            pass

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

if minimumWindow:
    pyautogui.moveTo(600, 3, 1)
    pyautogui.dragTo(0, 200, 1, button='left')

browser.get('https://en.wikipedia.org/wiki/Main_Page')
link = '/wiki/The_40-Year-Old_Virgin' 
e = browser.find_element_by_css_selector('[href^=]' + link)
location = e.location
size = e.size
print(location)
print(size)
a = browser.execute_script("return outerWidth")
c = browser.execute_script("return outerHeight - innerHeight")
b = browser.execute_script("return outerHeight")
pyautogui.moveTo(location['x']*1920/a, (location['y'] + c)*1080/b, 0.1)

(x, y) = pyautogui.position()

print(str(x) + " " + str(y) + "\n")