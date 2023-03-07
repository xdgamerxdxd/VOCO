import pygame
import sys
from clicker import *

pygame.init()

# ekraani suurus
screen_width = 1280
screen_height = 768

#värvid
white = (255, 255, 255)
red = (255, 0, 0)

# ekraan
screen = pygame.display.set_mode((screen_width, screen_height))

# ekraani nimi
pygame.display.set_caption("main menu")

# Font
smallfont = pygame.font.SysFont('Corbel',35)

# kirjutamis funktsioon
def text(string, color):
    return smallfont.render(string , True , color)

# menüü nupu funktsioon
def menu_button(x, y, size, screen, color):
    button = pygame.Rect(x, y, size, size - 100)
    pygame.draw.rect(screen, color, button)
    
# runnib kogu asja
while True:
    # hiire positsioon
    mx, my = pygame.mouse.get_pos()
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Paneb tõeseks nupu vajutusel
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
            if event.button == 0:
                click = True
    # värvib ekraani
    screen.fill(white)

    # nupu tava asukoht
    size = 150
    x = screen_width // 2 - size // 2
    y = screen_height // 2 - size // 2
    # nupud
    button = pygame.Rect(x, y, 200, 50)
    rect = pygame.draw.rect(screen, (255,0,0), button)
    button_2 = pygame.Rect(x + 325, y, 200, 50)
    rect_2 = pygame.draw.rect(screen, (255,0,0), button_2)
    button_3 = pygame.Rect(x -325, y, 200, 50)
    rect_3 = pygame.draw.rect(screen, (255,0,0), button_3)
    button_4 = pygame.Rect(x, y + 200, 200, 50)
    rect_4 = pygame.draw.rect(screen, (255,0,0), button_4)
    button_5 = pygame.Rect(x + 325, y + 200, 200, 50)
    rect_5 = pygame.draw.rect(screen, (255,0,0), button_5)
    button_6 = pygame.Rect(x - 325, y + 200, 200, 50)
    rect_6 = pygame.draw.rect(screen, (255,0,0), button_6)
    
    # vaatab kas hiir on nupul
    if button.collidepoint((mx, my)):
        if click:
            print('a')
    if button_2.collidepoint((mx, my)):
        if click:
            print('am')
    if button_3.collidepoint((mx, my)):
        if click:
            print('amo')
    if button_4.collidepoint((mx, my)):
        if click:
            print('amon')
    if button_5.collidepoint((mx, my)):
        if click:
            print('among')
    if button_6.collidepoint((mx, my)):
        if click:
            print('amongu')
    #uuendab
    pygame.display.update()
