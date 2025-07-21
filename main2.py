import pygame

screen_width = 800
screen_height = 600

# colours
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

fps = 60
pet_speed = 200
pet_radius = 100
pet_border_width = 2

left_boundary = 100
right_boundary = 700

state_duration_seconds = 3

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Improved Virtual Pet")
clock = pygame.time.Clock()

class Pet:
    def __init__(self, initial_x, initial_y, speed, state_duration):
        self.center = [initial_x, initial_y]
        self.state = "MOVING_RIGHT"
        self.hunger = 0
        self.speed = speed
        self._state_timer = 0.0
        self._state_duration = state_duration

    def _handle_movement(self, delta_time):
        if self.state == "MOVING_RIGHT":
            self.center[0] += self.speed * delta_time
            if self.center[0] >= right_boundary:
                self.center[0] = right_boundary
                self.state = "MOVING_LEFT"
                self._state_timer = 0.0
        elif self.state == "MOVING_LEFT":
            self.center[0] -= self.speed * delta_time
            if self.center[0] <= left_boundary:
                self.center[0] = left_boundary
                self.state = "IDLE"
                self._state_timer = 0.0

    def _handle_idle(self):
        if self.state == "IDLE":
            if self._state_timer >= self._state_duration:
                self.state = "MOVING_RIGHT"
                self._state_timer = 0.0

    def update(self, delta_time):
        self._state_timer += delta_time

        if self.state in ["MOVING_RIGHT", "MOVING_LEFT"]:
            self._handle_movement(delta_time)
        elif self.state == "IDLE":
            self._handle_idle()

    def draw(self, surface, color):
        pygame.draw.circle(surface, color, (int(self.center[0]), int(self.center[1])), pet_radius, pet_border_width)



pet = Pet(
    initial_x=screen_width // 2,
    initial_y=screen_height // 2,
    speed=pet_speed,
    state_duration=state_duration_seconds
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Window closed!")

    dt = clock.tick(fps) / 1000.0

    pet.update(dt)

    screen.fill(red)
    pet.draw(screen, white)

    pygame.display.flip()

pygame.quit()
