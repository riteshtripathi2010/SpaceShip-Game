
#First, installing pygame through Terminal
import pygame

#pygame is 2D graphics library to make games
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Step2
#How to draw on to the screen and change the name of that window
pygame.display.set_caption("First Game!")

#Step1
def main():
    #this will have loop, which will redrawn the window, checking for collisions, updating the scores
    #we dont want the game to instantly open and close, hence we use WHILE loop
    #think as in infinite loop and terminates whenever the game ends

    run = True    #when run becomes false, the loop will end
    while run:
        for event in pygame.event.get(): #different events occuring in pygame

            #first event is, if the user quit the window
            if event.type == pygame.QUIT:
                run =False   #this will end the WHILE loop
        
        #Filling the screen with color
        WIN.fill((255,255,255))#this is tuple for RGB, 3 values, WHITE color
        #after above, we need to update always for display
        pygame.display.update()

        #i dont want all of my drawings inside this main function
        #i usually want to have main game loop handling all of the collisions, all the logic in the game
        #and then having some of the functions outside of that i can easily call

    pygame.quit() #this will quit pygame for us


if __name__ == "__main__": #name: is the name of the file
    main()

