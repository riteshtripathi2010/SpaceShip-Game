import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60  # Standard
vel = 5  #Velocity to be used when left key is pressed, to move spaceship left

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
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


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

        #the method is to use multiple keys at same time
        #there are other methods to use one key at a time
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #Left
            yellow.x -= vel
        if keys_pressed[pygame.K_d]: #Right, need one position to the rightside
            yellow.x += vel
        if keys_pressed[pygame.K_w]:#isntead of x being modified, its y being modififed, y is the height
            yellow.y -= vel
        if keys_pressed[pygame.K_s]:
            yellow.y += vel





        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()

