#Now we have to add bullets, firing

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
BULLETS_VEL = 7 #we can make the speed of bullets to go fast or slow
MAX_BULLETS = 3

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

    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x:
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0 :
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15:
        yellow.y += vel

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x + BORDER.width:
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0:
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < HEIGHT - 15:
        red.y += vel

def main():

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []#normally we would use space bar to fire, but we have multiple people playing we cant use spacebar
                #we wil use left ctr and right ctr to fire bullets, and make sure caps lock isnt on while programming
                #i want each player to have limited number of bullets
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                #for bullets
            if event.type == pygame.KEYDOWN: #if pressed down key, fire the bullet
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: #len..is to make bullets that are fired and disappear before again 3 rounds of bullets can be fired
                    #if leftctrl, make bullets go right hand side of the screen
                    #we want the bullet to come out from the yellow body
                    #we want to create Rectangle at the position where we want to fire from, along with bullet to be placed after the yellow body
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)#this comes exactly in the middle of the character. 5 is the height of bullet, and 10 is the pixel of the bullet
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)#the red is facing to the left the screen, bullets will move towards left
                    red_bullets.append(bullet)

        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()

