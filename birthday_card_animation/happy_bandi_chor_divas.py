import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("happy divali") 

diva = pygame.image.load("images/diva_lamps_(1).jpeg")
diva = pygame.transform.scale(diva,(WIDTH,HEIGHT))

while True:
    font = pygame.font.SysFont("Times New Roman", 40)
    text_1 = font.render("Happy Divali", True, (0, 0, 0))
    text_2 = font.render("Happy Bandi Chor", True, (0, 0, 0))  
    screen.fill((255,255,255))
    screen.blit(diva,(0,0))
    screen.blit(text_1,(210,180))
    screen.blit(text_2,(180,265))
    pygame.display.update()
    time.sleep(3)

    bandi_chor =pygame.image.load("images/bandi_chor_divas.png")
    bandi_chor= pygame.transform.scale(bandi_chor,(WIDTH,HEIGHT))

    screen.fill((255,255,255))
    screen.blit(bandi_chor,(0,0))
    pygame.display.update()
    time.sleep(3)

    diwali = pygame.image.load("images/diwali.jpg")
    diwali = pygame.transform.scale(diwali,(WIDTH,HEIGHT)) 
    screen.fill((255,255,255))
    screen.blit(diwali,(0,0))
    pygame.display.update()
    time.sleep(3)









