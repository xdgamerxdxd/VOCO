import pygame
from sprites import *


class Point_Click():
    def __init__(self, state, screen):
        self.screen = screen
        self.running = state
        self.areas()
        
        pygame.display.set_caption("Point & Click")

    def areas(self):
        self.all = pygame.sprite.Group()
        self.uksed = Voco_uksed(1280, 768)
        self.all.add(self.uksed)

    def run(self):
        click = False
        while self.running:
            mx, my = pygame.mouse.get_pos()
    
        self.all.draw(self.screen)
        self.uksed.run()
        
   #     if self.test.rect.collidepoint((mx, my)):
    #        if click:
     #           self.screen.blit(pygame.image.load(f'{i}asendus fuajee.png'), (0, 0))

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
        
        