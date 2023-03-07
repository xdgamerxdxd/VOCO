import pygame
import sys

pygame.init()

screen_width = 1280
screen_height = 768

white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("main menu")

smallfont = pygame.font.SysFont('Corbel',35)

def text(string, color):
    return smallfont.render(string , True , color)
    

clock = pygame.time.Clock()

def menu_button(x, y, size, screen, color):
    button = pygame.Rect(x, y, size, size - 100)
    pygame.draw.rect(screen, color, button)
    

while True:
    mx, my = pygame.mouse.get_pos()
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
            if event.button == 0:
                click = True
    screen.fill(white)


    size = 150
    x = screen_width // 2 - size // 2
    y = screen_height // 2 - size // 2
    game = "game"
    color = (255,255,255)
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
    pygame.display.update()

    clock.tick(60)
