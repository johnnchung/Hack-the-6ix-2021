import pyautogui
import pyperclip


if __name__ == "__main__":
    pyautogui.click(0, 200)
    pyautogui.press('f6')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('f6')
    url = pyperclip.paste()
    print(url)
