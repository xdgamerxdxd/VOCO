import pygame
from sprites import *


class Point_Click():
    def __init__(self, screen, state):
        self.screen = screen
        self.running = state
        pygame.display.set_caption("Point & Click")

    def run(self):
        click = False
        while self.running:
            self.screen.blit(pygame.image.load(f'{i}voco_uksed.png'), (0, 0))
            mx, my = pygame.mouse.get_pos()
    

        if self.test.rect.collidepoint((mx, my)):
            if click:
                self.screen.blit(pygame.image.load(f'{i}asendus fuajee.png'), (0, 0))

        click = False       
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                    if event.button == 0:
                        click = True
                pygame.display.update()
        
        