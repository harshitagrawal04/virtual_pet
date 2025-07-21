import pygame
from pet_file import Pet

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


pet = Pet(
        pet_center_x,
        pet_center_y,
        pet_speed,
        pet_state_duration,
        pet_radius,
        pet_border_width)

running = True
while running:
    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Window closed!")

    dt = clock.tick(fps)/1000


    pet.update(dt, screen_width)

    screen.fill(red)
    pet.draw(screen)

    pygame.display.flip()


pygame.quit()