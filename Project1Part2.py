import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")

WHITE = (255,255,255)

FPS = 60 #Standard

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#Resize the Yellow Spaceship
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
#Resize the Yellow Spaceship
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window():#inside here i would take arguments that i would want to draw
    WIN.fill(WHITE)
    #WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100)) #use blit when u want to draw surface on to the screen
    #after defining and rotating with height and width, i have removed the above line, ie i am updating (Scaled Down Version)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    WIN.blit(RED_SPACESHIP, (700, 100)) #putting away distance from yellow space ship
    pygame.display.update()

def main():

    clock = pygame.time.Clock()#this is going to control the speed of my WHILE loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False 

        draw_window()
        #right now its displaying refresh rate on my computer with white color and at every 1 sec, its drawing white background, because my refresh rate is fast
        #but for other users it might not be the same
        #on different machines, it would run at a different speed
        #for this, we need to have a control on fps
    pygame.quit()

if __name__ == "__main__": 
    main()

