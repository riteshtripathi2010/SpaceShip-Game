#i want to have spaceships to have their own screen, like half of the screens owing to each other
import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)#we need to draw a rectangular on to the screen (On X, Y Position and Widht and Height,
#Y is going to be from 0 (thats the top most part of the screen, and Height should fill the entire screen) )
#WIDTH/2 = 900 / 2 = 450

FPS = 60
vel: int = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# Resize the Yellow Spaceship
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
# Resize the Yellow Spaceship
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    #i dont want the spaceship to cross the border line or on the left side of pane (not going to negative cordinates on left side)
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:#subtracting our current y posiition that will be greater than 0 or not, if it is, then we wont move any further to the left
        yellow.x -= vel #its minus, bse we are moving left
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x: #as we move right, it shouldnt cross the border
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0 :
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15: #this tells that the spaceship cant go further down the screenss
        yellow.y += vel

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x + BORDER.width: #this command will limit red to cross the border line towards the yellow
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:#this will let red to back on right side to its extreme of screen
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0:
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < HEIGHT - 15:
        red.y += vel

def main():

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()

