import pygame
import sys

pygame.init()

global width, height
screen_width = 1280
screen_height = 768

white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("main menu")

        
smallfont = pygame.font.SysFont('Corbel',35)
text_color = (255,255,255)
sentance = "GAME 1"
text = smallfont.render(sentance , True , text_color)
#font = font_class()

clock = pygame.time.Clock()

    
size = 150
x = screen_width // 2 - size // 2
y = screen_height // 2 - size // 2

# menu_button = menu_button_class()
menu_button_1 = pygame.Rect(x, y, size, size - 100)
menu_button_2 = pygame.Rect(x, y + 80,size, size - 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y+40:
                pygame.quit()

    screen.fill(white)

    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(screen, red, menu_button_1)
    pygame.draw.rect(screen, red, menu_button_2)

    screen.blit(text , (x,y))

    pygame.display.update()

    clock.tick(60)