import tkinter as tk
import mouse
from gui.animation import Animation
from pipeline.pipeline import Pipeline
from gui.companion_gui import Companion_Gui
from gui.cursor import Cursor
from gui.duck import Duck
import os
from PIL import Image, ImageTk

IM_PATH = os.getcwd() + "\\animations\\"

if __name__ == "__main__":
    window = tk.Tk()
    window1 = tk.Toplevel()
    window.attributes("-topmost", True)
    window.config(highlightbackground='black')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor','black')

    window1.attributes("-topmost", True)
    window1.config(highlightbackground='black')
    window1.overrideredirect(True)
    window1.wm_attributes('-transparentcolor','black')
    window1.config(cursor='none')

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
    poop_warning_animation = Animation(IM_PATH + 'Duck_warning.gif').frames

    image = Image.open(IM_PATH + 'cheese.png')
    image = ImageTk.PhotoImage(image)

    duck = Duck(50, 50, idle_animation, right_animation, left_animation, up_animation, down_animation,
                eat_left_animation, eat_right_animation, poop_left_animation, poop_right_animation, poop_warning_animation)

    pipeline = Pipeline(5, cursor)
    gui = Companion_Gui(window, pipeline, duck, cursor, window1, image)
    gui.play()
