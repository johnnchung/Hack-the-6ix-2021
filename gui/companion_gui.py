import pyautogui
import mouse
import os
import tkinter as tk
from PIL import Image, ImageTk

from gui.animation import Animation
from gui.duck import Duck
from gui.cursor import Cursor
from gui.state import State

HEIGHT = 220
WIDTH = 200

class Companion_Gui:
    def __init__(self, window, duck, cursor):
        self.window = window
        self.duck = duck
        self.cursor = cursor
        self.label = tk.Label(self.window, bd=0, bg='black')

    def play(self):
        self.window.after(1, self.update_frame)
        self.window.mainloop()

    def update_state(self):
        self.duck.movement_state()
        self.window.after(50, self.update_frame)

    def update_frame(self):
        self.cursor.modify_position()
        # self.detect_phishing()
        frame = self.duck.update_window(self.cursor.pos_x, self.cursor.pos_y)
        self.window.geometry(str(HEIGHT) + 'x' + str(WIDTH) + "+" + str(self.duck.pos_x) + '+' + str(self.duck.pos_y))
        self.label.configure(image=frame)
        self.label.pack()
        self.window.after(1, self.update_state)
    
