import pygame
import time
from sprites import *


class Point_Click():
    def __init__(self, state, screen):
        self.screen = screen
        self.running = state
        self.areas()
        
        pygame.display.set_caption("Point & Click")

    def areas(self):
        self.all = pygame.sprite.Group()
        self.uksed = Voco_uks(0, 0)
        self.fuajee = Voco_fuajee(0, 0)
        self.korridor = Voco_korridor(0, 0)
        self.trepp = Voco_trepp(0, 0)
        self.trepp2 = Voco_trepp2(0, 0)
        self.trep3 = Voco_trep3(0, 0)
        self.korrus3 = Voco_3korrus(0, 0)
        self.klass = Voco_klass(0, 0)
        self.joonas = Voco_joonas(0, 0)
        self.margus = Voco_margus(0, 0)
        self.all.add(self.uksed)

    def run(self):
        click = False
        while self.running:
            mx, my = pygame.mouse.get_pos()
    
            self.all.draw(self.screen)
            #self.uksed.run()
            
            if self.uksed.rect.collidepoint((mx, my)):
                if click:
                    self.all.add(self.margus)

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
            
            
        
        
