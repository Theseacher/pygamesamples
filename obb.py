import pygame
import random
#initialise screan
pygame.init

#set the width and hight
win = pygame.display.set_mode((800,600))

#the title
pygame.display.set_caption(("fake"))


#the icon
icon = pygame.image.load("/home/ibrahim/Programs/python-tutorial/pygame/tutorial/title.png")
pygame.display.set_icon(icon)

#wallpaper
background = pygame.image.load("/home/ibrahim/Programs/python-tutorial/pygame/tutorial/vecteezy_african-desert-landscape-background-for-game_12746791.jpg")

#the player
playerimg = pygame.image.load("/home/ibrahim/Programs/python-tutorial/pygame/tutorial/bird_wing_up.png")
playerx = 10
playery = 400
playerx_change = 0



def player(x,y):
    #the blit method draws the character
    win.blit(playerimg, (x,y))



#the enemy
ghostimg = pygame.image.load("/home/ibrahim/Programs/python-tutorial/pygame/angrybirds/ghost.png")
ghostx = 10
ghosty = 100
ghostx_change = 3



def ghost(x,y):
    #the blit method draws the character
    win.blit(ghostimg, (x,y))

#bullet
bulletimg = pygame.image.load("/home/ibrahim/Programs/python-tutorial/pygame/angrybirds/car.png")
bulletx = 0
bullety = 400
bullety_change = 10
bullet_active = "ready"


def bullet(x,y):
    global bullet_active
    bullet_active = 'go'
    #the blit method draws the character
    win.blit(bulletimg, (x - 3,y -16))







#the mainloop for everything that is going to happen on screen
active = True
while active:
       
    #the window color
    win.fill((25,40,50))
    
    #the background
    win.blit(background,(0,0))
    
    
    #a for loop for all events to get the quit event with an if statement to quit the screan
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            
    
        #checking the keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 10
            if event.key == pygame.K_RIGHT:
                playerx_change += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
               playerx_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                   bullet(playerx,bullety)
    
    
 
    #change the character position
    playerx += playerx_change
    
    #this is border
    if playerx <= 0:
       playerx = 0
    elif playerx >= 770:
       playerx = 770
    
    
    
    
    ghostx += ghostx_change
    
    #this is border
    if ghostx <= 0:
       ghostx_change += 3
       ghosty += 5
    elif ghostx >= 770:
       ghostx_change -= 3
       ghosty += 5
     #bullet movement
    if bullet_active is "go":
        bullet(playerx,bullety)
        bullety -= bullety_change
          
    
   
   
    
    #call enemy
    ghost(ghostx,ghosty)
    
    #call the player
    player(playerx,playery)
    
    #we have to update the screan to show the changes we make
    pygame.display.update()