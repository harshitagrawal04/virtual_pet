import pygame


class Pet:
    def __init__(self, center_x, center_y, speed, state_duration, radius, border_width,):
        self.center = [center_x, center_y]
        self.state = "MOVING_RIGHT"
        self.hunger = 0
        self.speed = speed
        self.hunger_speed = 10
        self.state_timer = 0
        self.state_duration = state_duration
        self.radius = radius
        self.border_width = border_width

    def handle_movement(self, delta_time, screen_width_):
        if self.state == "MOVING_RIGHT":
            self.center[0] += self.speed * delta_time
            if (self.center[0] > (screen_width_ - self.radius)) or (self.state_timer >= self.state_duration):
                self.state = "MOVING_LEFT"
                self.state_timer = 0
        elif self.state == "MOVING_LEFT":
            self.center[0] -= self.speed * delta_time
            if (self.center[0] <  self.radius) or (self.state_timer >= self.state_duration):
                self.state = "IDLE"
                self.state_timer = 0

    def handle_idle(self):
        if self.state_timer >= self.state_duration:
            self.state = "MOVING_RIGHT"
            self.state_timer = 0

    def handle_hunger(self, delta_time):
        if self.center[1] > 100:
            self.center[1] -= self.speed * delta_time
        else:
            self.hunger = 0
            self.state = "RETURN"
            self.state_timer = 0

    def handle_return(self, delta_time):
        if self.center[1] < 300:
            self.center[1] += self.speed * delta_time
        else:
            self.state = "IDLE"
            self.state_timer = 0

    def update(self, delta_time, screen_width_):
        self.state_timer += delta_time
        self.hunger += self.hunger_speed * delta_time
        print(self.hunger)
        if self.hunger >= 100:
            self.state = "HUNGER"
        if self.state in ["MOVING_LEFT", "MOVING_RIGHT"]:
            self.handle_movement(delta_time, screen_width_)
        elif self.state == "IDLE":
            self.handle_idle()
        elif self.state == "HUNGER":
            self.handle_hunger(delta_time)
        elif self.state == "RETURN":
            self.handle_return(delta_time)

    def get_color(self):
        if self.state == "HUNGER" or self.state == "RETURN":
            return 255, 255, 0
        return 255, 255, 255

    def draw(self, surface):
        colour = self.get_color()
        pygame.draw.circle(surface, colour, self.center, self.radius, self.border_width)
