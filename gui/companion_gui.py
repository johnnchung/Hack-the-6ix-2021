import pyautogui
import mouse
import os
import tkinter as tk

from PIL import Image, ImageTk

from animation import Animation
from duck import Duck
from cursor import Cursor
from state import State


IM_PATH = os.getcwd() + "\\..\\animations\\"
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
        self.detect_phishing()
        frame = self.duck.update_window(self.cursor.pos_x, self.cursor.pos_y)
        self.window.geometry(str(HEIGHT) + 'x' + str(WIDTH) + "+" + str(self.duck.pos_x) + '+' + str(self.duck.pos_y))
        self.label.configure(image=frame)
        self.label.pack()
        self.window.after(1, self.update_state)
    
    def detect_phishing(self, linkArray):
        for link in linkArray: 
            if link.checkbox(cursor.pos_x, cursor.pos_y):
                return link
        return None

if __name__ == "__main__":
    window = tk.Tk()
    # window.config(highlightbackground='black')
    # window.overrideredirect(True)
    # window.wm_attributes('-transparentcolor','black')

    x, y = mouse.get_position()
    cursor = Cursor(x, y)

    idle_animation = Animation(IM_PATH + 'Duck_idle.gif').frames
    right_animation = Animation(IM_PATH + 'Duck_right.gif').frames
    left_animation = Animation(IM_PATH + 'Duck_left.gif').frames
    up_animation = Animation(IM_PATH + 'Duck_up.gif').frames
    down_animation = Animation(IM_PATH + 'Duck_down.gif').frames
    eat_right_animation = Animation(IM_PATH + 'Duck_eat_right.gif').frames
    eat_left_animation = Animation(IM_PATH + 'Duck_eat_left.gif').frames
    poop_left_animation = Animation(IM_PATH + 'Duck_poop_left2.gif').frames
    poop_right_animation = Animation(IM_PATH + 'Duck_poop_right2.gif').frames
    duck = Duck(x, y, idle_animation, right_animation, left_animation, up_animation, down_animation,
                eat_left_animation, eat_right_animation, poop_left_animation, poop_right_animation)

    gui = Companion_Gui(window, duck, cursor)
    gui.play()
