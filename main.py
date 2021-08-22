import tkinter as tk
import mouse
from gui.animation import Animation
from pipeline.pipeline import Pipeline
from gui.companion_gui import Companion_Gui
from gui.cursor import Cursor
from gui.duck import Duck
import os
    
IM_PATH = os.getcwd() + "\\animations\\"
    
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

    pipeline = Pipeline(5, gui)
    pipeline.play()