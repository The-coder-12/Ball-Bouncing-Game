import pygame
import sys
import random
import time

clock = pygame.time.Clock()

#Initialize pygame
pygame.init()

#Display variables
x = 1550
y = 800
bg = pygame.image.load("sky.jpeg")
bg1 = pygame.transform.scale(bg, (x, y))

#Sound
pygame.mixer_music.load("jews_harp_boing-7111.mp3")

#Create the display
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Ball Bouncing Animation (v2)")

#Main variable
run = False

def create_balls():
    speed = [random.randint(1, 2), random.randint(1, 5)]
    radius = random.randint(10, 30)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    position = [random.randint(radius, x-radius), random.randint(radius, y-radius)]
    return {"radius": radius, "color": color, "speed": speed, "position": position}

multiple_balls = [create_balls() for i in range(10)]

#Main loop
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    #Update the positions of the balls
    for ball in multiple_balls:
        ball["position"][0] += ball["speed"][0]
        ball["position"][1] += ball["speed"][1]

        # Set the boundary to bounce the balls
        if ball["position"][0] <= 0 or ball["position"][0] >= x:
            ball["speed"][0] = -ball["speed"][0]
            pygame.mixer_music.play()

        if ball["position"][1] <= 0 or ball["position"][1] >= y:
            ball["speed"][1] = -ball["speed"][1]
            pygame.mixer_music.play()

    #Fill the display with the bg image
    screen.blit(bg1, [0, 0])
    #Simple ball designs
    for ball in multiple_balls:
        pygame.draw.circle(screen, ball["color"], (ball["position"][0], ball["position"][1]), ball["radius"])

    pygame.display.update()

    clock.tick(4800)

#Close the window and stop the code
pygame.quit()
quit()