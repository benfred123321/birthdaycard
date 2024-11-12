import pygame
import time 

pygame.init()

WIDTH=600
HIEGHT=600 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("birthdaycard")

while True:
    #in pygame in order to use image we have to paform two steps 
    #step 1 - Loading
    image1 = pygame.image.load("backgroundone.jpg")
    screen.fill("white")
    #step 2 displaying
    screen.blit(image1,(0,0))
    pygame.display.update()
    time.sleep(2)