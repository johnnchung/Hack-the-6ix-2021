import pyautogui
import mouse
import tkinter as tk
from PIL import Image, ImageTk

from animation import Animation
from goose import Goose
from cursor import Cursor


IM_PATH = 'C:\\Users\\chera\\Cheran\\GitHub\\Hack-the-6ix-2021\\animations\\'
HEIGHT = 200
WIDTH = 200


class Companion_Gui:
    def __init__(self, window, goose, cursor):
        self.window = window
        self.goose = goose
        self.cursor = cursor
        self.label = tk.Label(self.window, bd=0, bg='black')

    def play(self):
        self.window.after(1, self.update_frame)
        self.window.mainloop()

    def update_state(self):
        self.goose.movement_state()
        self.window.after(50, self.update_frame)

    def update_frame(self):
        self.cursor.modify_position()
        frame = self.goose.update_window(self.cursor.pos_x, self.cursor.pos_y)
        self.window.geometry(str(HEIGHT) + 'x' + str(WIDTH) + "+" + str(self.goose.pos_x) + '+' + str(self.goose.pos_y))
        self.label.configure(image=frame)
        self.label.pack()
        self.window.after(1, self.update_state)


if __name__ == "__main__":
    window = tk.Tk()
    # window.config(highlightbackground='black')
    # window.overrideredirect(True)
    # window.wm_attributes('-transparentcolor','black')

    x, y = mouse.get_position()
    cursor = Cursor(x, y)

    idle_animation = Animation(IM_PATH + 'idle.gif').frames
    right_animation = Animation(IM_PATH + 'Duck_right.gif').frames
    left_animation = Animation(IM_PATH + 'Duck_left.gif').frames
    up_animation = Animation(IM_PATH + 'up.gif').frames
    down_animation = Animation(IM_PATH + 'Duck_down.gif').frames
    goose = Goose(x, y, idle_animation, right_animation, left_animation, up_animation, down_animation)

    gui = Companion_Gui(window, goose, cursor)
    gui.play()
