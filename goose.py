from state import State

WIDTH = 350
HEIGHT = 350


class Goose:
    def __init__(self, pos_x, pos_y, idle_anim, run_anim, up_anim, down_anim):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.idle_anim = idle_anim
        self.run_anim = run_anim
        self.up_anim = up_anim
        self.down_anim = down_anim
        self.check = 0
        self.cycle = 0
        self.event_number = State.IDLE_EVENT

    def movement_state(self):
        if self.event_number == State.IDLE_EVENT:
            self.check = 0
        elif self.event_number == State.RUN_LEFT_EVENT:
            self.check = 1
            print('walking left')
        elif self.event_number == State.RUN_RIGHT_EVENT:
            self.check = 2
            print('walking right')
        elif self.event_number == State.RUN_UP_EVENT:
            self.check = 3
            print('walking up')
        elif self.event_number == State.RUN_DOWN_EVENT:
            self.check = 4
            print('walking down')

    def gif_work(self, frames, cursor_x, cursor_y):
        if self.cycle < len(frames) - 1:
            self.cycle += 1
        else:
            self.cycle = 0

        new_orientation = self.orientation(cursor_x, cursor_y)
        if new_orientation != self.event_number:
            self.event_number = new_orientation
            self.cycle = 0

    def update_window(self, cursor_x, cursor_y):
        if self.check == 0:
            frame = self.idle_anim[self.cycle]
            self.gif_work(self.idle_anim, cursor_x, cursor_y)
        elif self.check == 1:
            frame = self.run_anim[self.cycle]
            self.gif_work(self.run_anim, cursor_x, cursor_y)
            self.pos_x -= 10
        elif self.check == 2:
            frame = self.run_anim[self.cycle]
            self.gif_work(self.run_anim, cursor_x, cursor_y)
            self.pos_x += 10
        elif self.check == 3:
            frame = self.up_anim[self.cycle]
            self.gif_work(self.up_anim, cursor_x, cursor_y)
            self.pos_y += 10
        elif self.check == 4:
            frame = self.down_anim[self.cycle]
            self.gif_work(self.down_anim, cursor_x, cursor_y)
            self.pos_y -= 10
        return frame

    def orientation(self, cursor_x, cursor_y, idle=False):
        print(self.pos_y, cursor_y)
        if idle or (0 < self.pos_x - cursor_x < 40 and 0 < self.pos_y - cursor_y < 40) or 0 < cursor_x - self.pos_x < WIDTH + 40:
            return State.IDLE_EVENT

        if cursor_x > self.pos_x:
            return State.RUN_RIGHT_EVENT
        if cursor_x < self.pos_x:
            return State.RUN_LEFT_EVENT
    
    def is_in_hitbox(self, cursor_x, cursor_y, buffer):
        if self.pos_x - buffer < cursor_x < self.pos_x + WIDTH + buffer and self.pos_y - buffer < cursor_y < self.pos_y + HEIGHT + buffer:
            return True
        else:
            return False

    def control_mouse(self, cursor, direction):
        pass
