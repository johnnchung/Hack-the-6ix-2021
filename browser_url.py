import pyautogui
import pyperclip

def get_browser_url(): 
    try:
        pyautogui.press('f6')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('f6')
        url = pyperclip.paste()
        print(url)
        if('https' in url):
            return url
        return None
    except:
        return None