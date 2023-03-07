import pygame
import sys
from clicker import text_thing

pygame.init()

# menüü nupu funktsioon
class Menu_button():
    def __init__(self, x, y, sizex, sizey, screen, color, color1, text):
        button = pygame.Rect(x, y, sizex, sizey)
        self.rect = pygame.draw.rect(screen, color, button)
        text_thing(text, screen, smallfont, color1, self.rect.centerx, self.rect.centery)


global screen_height, screen_width, white, red, black, smallfont

# ekraani suurus
screen_width = 1280
screen_height = 768

#värvid
white = (255, 255, 255)
red = (255, 150, 100)
black = (0, 0, 0)
    
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
            x = 490
            y = 170
            sizex = 320
            sizey = 80

            # nupud

            button = Menu_button(x, y, sizex, sizey, self.screen, red, black, 'Clicker')
            button1 = Menu_button(x + 400, y, sizex, sizey, self.screen, red, black, 'B')
            button2 = Menu_button(x - 400, y, sizex, sizey, self.screen, red, black, 'A')
            button3 = Menu_button(x, y + 340, sizex, sizey, self.screen, red, black, 'D')
            button4 = Menu_button(x + 400, y + 340, sizex, sizey, self.screen, red, black, 'E')
            button5 = Menu_button(x - 400, y + 340, sizex, sizey, self.screen, red, black, 'C')
            
            # vaatab kas hiir on nupul
            if button.rect.collidepoint((mx, my)):
                if click:
                    print('Clicker')
            if button1.rect.collidepoint((mx, my)):
                if click:
                    print('B')
            if button2.rect.collidepoint((mx, my)):
                if click:
                    print('A')
            if button3.rect.collidepoint((mx, my)):
                if click:
                    print('D')
            if button4.rect.collidepoint((mx, my)):
                if click:
                    print('E')
            if button5.rect.collidepoint((mx, my)):
                if click:
                    print('C')

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