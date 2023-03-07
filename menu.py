import pygame
import sys
#from clicker import *

pygame.init()

# kirjutamis funktsioon
def text(string, color):
    return smallfont.render(string , True , color)

# menüü nupu funktsioon
def menu_button(x, y, size, screen, color):
    button = pygame.Rect(x, y, size, size - 100)
    pygame.draw.rect(screen, color, button)


global screen_height, screen_width, white, red

# ekraani suurus
screen_width = 1280
screen_height = 768

#värvid
white = (255, 255, 255)
red = (255, 150, 100)
    
# Font
smallfont = pygame.font.SysFont('Calibri',35)


class Main_menu():
    def __init__(self, screen):
        self.screen = screen
        self.runn = True
        # ekraani nimi
        pygame.display.set_caption("main menu")

    def run(self):
        click = False
        while self.runn:
            # hiire positsioon

            mx, my = pygame.mouse.get_pos()


            # värvib ekraani
            self.screen.fill(white)

            # nupu tava asukoht
            possize = 100
            x = 490
            y = 170
            sizex = 320
            sizey = 80

            # nupud
            button = pygame.Rect(x, y, sizex, sizey)
            rect = pygame.draw.rect(self.screen, red, button)
            button_2 = pygame.Rect(x + 400, y, sizex, sizey)
            rect_2 = pygame.draw.rect(self.screen, red, button_2)
            button_3 = pygame.Rect(x -400, y, sizex, sizey)
            rect_3 = pygame.draw.rect(self.screen, red, button_3)
            button_4 = pygame.Rect(x, y + 340, sizex, sizey)
            rect_4 = pygame.draw.rect(self.screen, red, button_4)
            button_5 = pygame.Rect(x + 400, y + 340, sizex, sizey)
            rect_5 = pygame.draw.rect(self.screen, red, button_5)
            button_6 = pygame.Rect(x - 400, y + 340, sizex, sizey)
            rect_6 = pygame.draw.rect(self.screen, red, button_6)
            
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
            pygame.display.update()