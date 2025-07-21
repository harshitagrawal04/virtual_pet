import pygame


# declaring the variables and constant
# screen
screen_width = 800
screen_height = 600
fps = 60

# colours
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# circle
pet_center_x = 300
pet_center_y = 300
pet_speed = 200
pet_radius = 100
pet_border_width = 2
pet_state = "MOVING_RIGHT"
pet_state_duration = 3


# setting up window
pygame.init() #initalising the library
screen = pygame.display.set_mode((screen_width, screen_height)) #crete the screen
clock = pygame.time.Clock()

class Pet:
    def __init__(self, center_x, center_y, speed, state_duration, radius, border_width, _screen_width, _screen_height):
        self.center = [center_x, center_y]
        self.state = "MOVING_RIGHT"
        self.hunger = 0
        self.speed = speed
        self.state_timer = 0
        self.state_duration = state_duration
        self.radius = radius
        self.border_width = border_width
        self.screen_width = _screen_width
        self.screen_height = _screen_height

    def handle_movement(self, delta_time):
        if self.state == "MOVING_RIGHT":
            self.center[0] += self.speed * delta_time
            if (self.center[0] > (self.screen_width - self.radius)) or (self.state_timer >= self.state_duration):
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

    def update(self, delta_time):
        self.state_timer += delta_time
        if self.state in ["MOVING_LEFT", "MOVING_RIGHT"]:
            self.handle_movement(delta_time)
        elif self.state == "IDLE":
            self.handle_idle()


    def draw(self, surface, colour):
        pygame.draw.circle(surface, colour, self.center, self.radius, self.border_width)



pet = Pet(
        pet_center_x,
        pet_center_y,
        pet_speed,
        pet_state_duration,
        pet_radius,
        pet_border_width,
        screen_width,
        screen_height)

running = True
while running:
    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Window closed!")

    dt = clock.tick(fps)/1000


    pet.update(dt)

    screen.fill(red)
    pet.draw(screen, white)

    pygame.display.flip()


pygame.quit()