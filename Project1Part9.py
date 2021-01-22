#now, lets check the event, when red or yellow get hit, what should be done
#and display health


import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
#the // whereever its placed, so that we dont have any floating point issues, we need them in integer
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)#we need to draw a rectangular on to the screen (On X, Y Position and Widht and Height,
#Y is going to be from 0 (thats the top most part of the screen, and Height should fill the entire screen) )
#WIDTH/2 = 900 / 2 = 450

HEALTH_FONT = pygame.font.SysFont('comicscans', 40)

FPS = 60
vel: int = 5
BULLETS_VEL = 7 #we can make the speed of bullets to go fast or slow
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT +2
#above now we have described there are two different players
#USEREVENT is a number and we are adding 1 to make it a unique id

red_health = 10
yellow_health = 10

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# Resize the Yellow Spaceship
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
# Resize the Yellow Spaceship
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    #WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)#render means: show 'health' as text, always put 1 as it as and color of health should be 'white'
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

    #we have created two text objects, now need to draw it
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))#extreme right side of the screen it would be displayed, minus 10 pixels (this 10 is from right wall), 10 pixels down (this 10 is from top wall)
    WIN.blit(yellow_health_text, (10, 10))#its the left border that will be padded with left wall, and 10 pixels down from top

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))



    #we are drawing the bullet on to the screen for red and yellow
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet )

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet )

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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):#move the bullets, handle the collison of bullets and handle removing bullets off the screen
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL #since its coming from Yellow, it should move from left to right, and after that we need to check for collisions
        if red.colliderect(bullet):#we need to tell main function, if bullet collided with red player, it should remove the health
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL #we need to change direction as its coming from red to yellow, left side
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

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
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)#this comes exactly in the middle of the character. 5 is the height of bullet, and 10 is the pixel of the bullet
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)#the red is facing to the left the screen, bullets will move towards left
                    red_bullets.append(bullet)

            #this is where it starts, we want both players to have health and once get hit, their number gets subtracted by 1
            if event.type == RED_HIT:
                red_health = red_health - 1

            if event.type == YELLOW_HIT:
                yellow_health = yellow_health - 1

        #check health of each player, if either one has 0, the opposite will win
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins"

        if yellow_health <= 0:
            winner_text = "Red Wins"

        if winner_text != "":
            pass #Someone one

        #print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)


        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)#we have to show score

    pygame.quit()

if __name__ == "__main__":
    main()

