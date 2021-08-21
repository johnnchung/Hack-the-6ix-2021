import pyautogui
import pyperclip
from timeit import default_timer

def set_interval(second_delay):
    start = default_timer()
    while True:
        duration = default_timer() - start
        if duration > second_delay:
            searchLinks()
            start = default_timer()

def searchLinks(): 
    pyautogui.press('f6')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('f6')
    url = pyperclip.paste()
    print(url)


if __name__ == "__main__":
    set_interval(5)
    #pyautogui.click(0, 200)
    # pyautogui.press('f6')
    # pyautogui.hotkey('ctrl', 'c')
    # pyautogui.press('f6')
    # url = pyperclip.paste()
    # print(url)
