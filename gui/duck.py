from state import State

WIDTH = 200
HEIGHT = 220
DUCK_SPEED = 20


class Duck:
    def __init__(self, pos_x, pos_y, idle_anim, right_anim, left_anim, up_anim, down_anim, digest_left_anim,
                 digest_right_anim, poop_left_anim, poop_right_anim):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.idle_anim = idle_anim
        self.right_anim = right_anim
        self.left_anim = left_anim
        self.up_anim = up_anim
        self.down_anim = down_anim
        self.digest_left_anim = digest_left_anim
        self.digest_right_anim = digest_right_anim
        self.poop_left_anim = poop_left_anim
        self.poop_right_anim = poop_right_anim
        self.check = 0
        self.cycle = 0
        self.event_number = State.IDLE_EVENT
        self.x_increment = 0
        self.y_increment = 0
        self.digestion_stage = 0
        self.repetitions = 0
        self.is_hiding = False

    def movement_state(self):
        if self.event_number == State.IDLE_EVENT:
            self.check = 0
        elif self.event_number == State.RUN_LEFT_EVENT:
            self.check = 1
        elif self.event_number == State.RUN_RIGHT_EVENT:
            self.check = 2
        elif self.event_number == State.RUN_UP_EVENT:
            self.check = 3
        elif self.event_number == State.RUN_DOWN_EVENT:
            self.check = 4
        elif self.event_number == State.MOUSE_DIGESTION_LEFT_EVENT:
            self.check = 5
        elif self.event_number == State.MOUSE_DIGESTION_RIGHT_EVENT:
            self.check = 6
        elif self.event_number == State.MOUSE_CONSTIPATION_LEFT_EVENT:
            self.check = 7
        elif self.event_number == State.MOUSE_CONSTIPATION_RIGHT_EVENT:
            self.check = 8
        elif self.event_number == State.MOUSE_POOP_LEFT_EVENT:
            self.check = 9
        elif self.event_number == State.MOUSE_POOP_RIGHT_EVENT:
            self.check = 10

    def gif_work(self, frames, cursor_x, cursor_y):
        if self.event_number in [State.MOUSE_POOP_LEFT_EVENT, State.MOUSE_POOP_RIGHT_EVENT] and self.cycle == len(frames) - 1:
            self.digestion_stage = 0
            self.event_number = State.IDLE_EVENT

        if self.event_number in [State.MOUSE_DIGESTION_LEFT_EVENT, State.MOUSE_DIGESTION_RIGHT_EVENT] and self.cycle == len(frames) - 1:
            if self.event_number == State.MOUSE_DIGESTION_LEFT_EVENT:
                self.event_number = State.MOUSE_CONSTIPATION_LEFT_EVENT
            else:
                self.event_number = State.MOUSE_CONSTIPATION_RIGHT_EVENT
            self.digestion_stage = 1
        
        if self.event_number in [State.MOUSE_CONSTIPATION_LEFT_EVENT, State.MOUSE_CONSTIPATION_RIGHT_EVENT] and self.cycle == len(frames) - 1 and self.repetitions%3 == 2:
            if self.event_number == State.MOUSE_CONSTIPATION_LEFT_EVENT:
                self.event_number = State.MOUSE_POOP_RIGHT_EVENT
            else:
                self.event_number = State.MOUSE_POOP_LEFT_EVENT
            self.digestion_stage = 2
            self.repetitions = 0

        if self.event_number in [State.MOUSE_CONSTIPATION_LEFT_EVENT, State.MOUSE_CONSTIPATION_RIGHT_EVENT] and self.cycle == len(frames) - 1:
            self.repetitions += 1

        if self.cycle < len(frames) - 1:
            self.cycle += 1
        else:
            self.cycle = 0

        if self.event_number in [State.MOUSE_POOP_LEFT_EVENT, State.MOUSE_POOP_RIGHT_EVENT]:
            new_orientation = self.event_number
        else:
            new_orientation = self.orientation(cursor_x, cursor_y, 50)
        if new_orientation != self.event_number:
            self.event_number = new_orientation
            self.cycle = 0

    def update_window(self, cursor_x, cursor_y):
        if self.check == 0:
            frame = self.idle_anim[self.cycle]
            self.gif_work(self.idle_anim, cursor_x, cursor_y)
        elif self.check == 1:
            frame = self.left_anim[self.cycle]
            self.gif_work(self.left_anim, cursor_x, cursor_y)
            self.pos_x += self.x_increment
            self.pos_y += self.y_increment
        elif self.check == 2:
            frame = self.right_anim[self.cycle]
            self.gif_work(self.right_anim, cursor_x, cursor_y)
            self.pos_x += self.x_increment
            self.pos_y += self.y_increment
        elif self.check == 3:
            frame = self.up_anim[self.cycle]
            self.gif_work(self.up_anim, cursor_x, cursor_y)
            self.pos_y += self.y_increment
        elif self.check == 4:
            frame = self.down_anim[self.cycle]
            self.gif_work(self.down_anim, cursor_x, cursor_y)
            self.pos_y += self.y_increment
        elif self.check == 5:
            frame = self.digest_left_anim[self.cycle]
            self.gif_work(self.digest_left_anim, cursor_x, cursor_y)
        elif self.check == 6:
            frame = self.digest_right_anim[self.cycle]
            self.gif_work(self.digest_right_anim, cursor_x, cursor_y)
        elif self.check == 7:
            self.pos_x += self.x_increment
            frame = self.right_anim[self.cycle]
            self.gif_work(self.right_anim, cursor_x, cursor_y)
        elif self.check == 8:
            self.pos_x += self.x_increment
            frame = self.left_anim[self.cycle]
            self.gif_work(self.left_anim, cursor_x, cursor_y)
        elif self.check == 9:
            frame = self.poop_left_anim[self.cycle]
            self.gif_work(self.poop_left_anim, cursor_x, cursor_y)
        elif self.check == 10:
            frame = self.poop_right_anim[self.cycle]
            self.gif_work(self.poop_right_anim, cursor_x, cursor_y)
        return frame

    def orientation(self, cursor_x, cursor_y, buffer):
        if self.is_idle:
            self.x_increment = 0
            self.y_increment = 0
            return State.IDLE_EVENT

        if self.digestion_stage == 0 and self.is_in_hitbox(cursor_x, cursor_y, buffer):
            self.x_increment = 0
            self.y_increment = 0
            if self.pos_x > cursor_x:
                return State.MOUSE_DIGESTION_LEFT_EVENT
            else:
                return State.MOUSE_DIGESTION_RIGHT_EVENT

        if self.digestion_stage == 1:
            if self.event_number == State.MOUSE_CONSTIPATION_LEFT_EVENT:
                self.x_increment = DUCK_SPEED
                self.y_increment = 0
            else:
                self.x_increment = -DUCK_SPEED
                self.y_increment = 0
            return self.event_number
        
        if self.digestion_stage == 2:
            self.x_increment = 0
            self.y_increment = 0
            return self.event_number

        if cursor_x > self.pos_x + WIDTH + buffer and cursor_y < self.pos_y - buffer:
            self.x_increment = DUCK_SPEED
            self.y_increment = -DUCK_SPEED
            return State.RUN_RIGHT_EVENT
        if cursor_x > self.pos_x + WIDTH + buffer and cursor_y > self.pos_y + HEIGHT + buffer:
            self.x_increment = DUCK_SPEED
            self.y_increment = DUCK_SPEED
            return State.RUN_RIGHT_EVENT
        if cursor_x < self.pos_x - buffer and cursor_y < self.pos_y - buffer:
            self.x_increment = -DUCK_SPEED
            self.y_increment = -DUCK_SPEED
            return State.RUN_LEFT_EVENT
        if cursor_x < self.pos_x - buffer and cursor_y > self.pos_y + HEIGHT + buffer:
            self.x_increment = -DUCK_SPEED
            self.y_increment = DUCK_SPEED
            return State.RUN_LEFT_EVENT
        if cursor_x > self.pos_x + WIDTH + buffer:
            self.x_increment = DUCK_SPEED
            self.y_increment = 0
            return State.RUN_RIGHT_EVENT
        if cursor_x < self.pos_x - buffer:
            self.x_increment = -DUCK_SPEED
            self.y_increment = 0
            return State.RUN_LEFT_EVENT
        if cursor_y > self.pos_y + HEIGHT + buffer:
            self.x_increment = 0
            self.y_increment = DUCK_SPEED
            return State.RUN_DOWN_EVENT
        if cursor_y < self.pos_y - buffer:
            self.x_increment = 0
            self.y_increment = -DUCK_SPEED
            return State.RUN_UP_EVENT

        return State.IDLE_EVENT

    def is_in_hitbox(self, cursor_x, cursor_y, buffer):
        if self.pos_x - buffer < cursor_x < self.pos_x + WIDTH + buffer and self.pos_y - buffer < cursor_y < self.pos_y + HEIGHT + buffer:
            return True
        else:
            return False

    def control_mouse(self, cursor, direction):
        pass
