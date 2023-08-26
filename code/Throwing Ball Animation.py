# Imports
import pygame
import time
import math
import sys

# Define constants
BG_COLOUR = (0, 0, 255)
BLACK = (0, 0, 0)
WINDOW_WIDTH =  1920
WINDOW_HEIGHT = 1080
DELAY = 0
BALL_WIDTH = 20
BALL_HEIGHT = 20
SCALE_FACTOR = 7
OMEGA = 1 / SCALE_FACTOR 
g = 9.81 / SCALE_FACTOR
v = 100 / SCALE_FACTOR 

# Define variables
ball_x = 410
ball_y = 1080 - 300 # Account for height of person
trail= [(ball_x + 15, ball_y + 15)] # Account for dimensions of ball

# Define ball and position
def draw_ball(x, y):
    ball = pygame.image.load('ball.png')
    screen.blit(pygame.transform.scale(ball, (30, 30)), (x, y))

# Define person and position
def draw_person():
    person = pygame.image.load('improved_person.png')
    screen.blit(pygame.transform.scale(person, (150, 300)), (350, 1080 - 300))

# Write majority of code in main function
def main():
    global screen, ball_x, ball_y # We want these variables to change globally
    open_waited = False
    while True:
        # Setup window and background
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.time.Clock()
        screen.fill(BG_COLOUR)
        
        # Want to delay the start to record a video
        if(open_waited == False):
            time.sleep(DELAY) 
            open_waited = True
        
        # To quit window without errors
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Draw the person and get the position of the ball and update
        draw_person()
        t = (pygame.time.get_ticks() - (1000 * DELAY)) / 1000
        draw_ball(ball_x, ball_y)
        trail.append((ball_x + 15,ball_y + 15))
        pygame.draw.lines(screen, BLACK, False, trail)
        ball_x = 410 + 20 * ((v / (2 * OMEGA)) + ((g * math.sin(2 * OMEGA * t)) / (4 * (OMEGA ** 2))) - \
                 ((v * math.cos(2 * OMEGA * t)) / (2 * OMEGA)) - ((g * t) / (2 * OMEGA)))
        ball_y = (1080 - 300) - 20 * (-(g / (4 * (OMEGA ** 2))) + ((v * math.sin(2 * OMEGA * t)) / \
                 (2 * OMEGA)) + ((g * math.cos(2 * OMEGA * t)) / (4 * (OMEGA ** 2))))
        pygame.display.update()

if __name__ == "__main__":
    main()