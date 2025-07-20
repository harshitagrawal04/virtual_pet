import pygame

pygame.init() #initalising the library
screen = pygame.display.set_mode((800, 600)) #crete the screen
clock = pygame.time.Clock()

running = True
center = [300, 300]
speed = 200
fps = 60
tracked_time = 0
state = "MOVING_RIGHT"

while running:
    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Window closed!")

    screen.fill((255, 0, 0))
    dt = clock.tick(fps)/1000
    tracked_time += dt

    if state == "MOVING_RIGHT":
        center[0] += speed * dt
        if center[0]>700 or tracked_time >= 3:
            state = "MOVING_LEFT"
            tracked_time = 0
    elif state == "MOVING_LEFT":
        center[0] -= speed * dt
        if center[0]<100 or tracked_time >= 3:
            state = "IDLE"
            tracked_time = 0
    elif state == "IDLE":
        if tracked_time >= 3:
            state = "MOVING_RIGHT"
            tracked_time = 0


    pygame.draw.circle(screen, (255, 255, 255), center, 100, 2)


    pygame.display.flip()


pygame.quit()