import pyautogui
import pyperclip
import keypress
import time, threading
from splinter import Browser
from selenium import webdriver

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def searchLinks(): 
        # pyautogui.press('f6')
        keyboard.press('f6')
        keyboard.press('ctrl', 'c')
        keyboard.press('f6')
        # pyautogui.hotkey('ctrl', 'c')
        # pyautogui.press('f6')
        url = pyperclip.paste()
        print(url)

set_interval(searchLinks, 1)


# driver = webdriver.Chrome()

# print(driver.current_url)
# stop = True 
# def searchLinks():
#     count = 0
#     while stop == True: 
#         if __name__ == '__main__':
#             count +=1 
#             pyautogui.click(0, 200)
#             pyautogui.press('f6')
#             pyautogui.hotkey('ctrl', 'c')
#             pyautogui.press('f6')
#             url = pyperclip.paste()
#             print(url)
# searchLinks()

# def stopBrowser(): 
#     stop = True
# def setInterval(interval):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             stopped = threading.Event()

#             def loop(): # executed in another thread
#                 while not stopped.wait(interval): # until stopped
#                     function(*args, **kwargs)

#             t = threading.Thread(target=loop)
#             t.daemon = True # stop if the program exits
#             t.start()
#             return stopped
#         return wrapper
#     return decorator

# @setInterval(1)
# def searchLinks(): 
#     if __name__ == '__main__':
#         pyautogui.click(0, 200)
#         pyautogui.press('f6')
#         pyautogui.hotkey('ctrl', 'c')
#         pyautogui.press('f6')
#         url = pyperclip.paste()
#         print(url)

# start_stop = searchLinks() # start timer, the first call is in 1 second
