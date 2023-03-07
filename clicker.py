import pygame
from pygame.locals import *
from sprites import * 

def text_thing(sentance, surface, font, color, x, y,):
    text = font.render(sentance, 1, color)
    rect = text.get_rect()
    rect.centerx = x
    rect.centery = y
    surface.blit(text, rect)

class Clicker():
    def __init__(self, screen):
        self.screen = screen
        self.running = False
        self.entities()
        self.clike = False
        self.score = 0
        self.workers = 0
        self.tick = pygame.time.get_ticks()
        self.ammount = 50

    def entities(self):
        self.all = pygame.sprite.Group()
        self.worker = Worker(200, 300)
        self.test = Test(1280, 768)
        self.all.add(self.test, self.worker)

    def run(self):
        mx, my = pygame.mouse.get_pos()
        self.all.draw(self.screen)
        self.test.run()
        self.working(self.workers)

        if self.worker.rect.collidepoint((mx, my)):
            text_thing('Vocos on kokku 75 kursust', self.screen, pygame.font.SysFont('Calibri', 20), (255,255,255), mx + 50, my)
            if self.clike and self.score >= self.ammount:
                self.workers += 1
                self.score -= self.ammount
                self.ammount += 3

        if self.test.rect.collidepoint((mx, my)):
            text_thing("Õppetöö toimub nii päeva- kui kaugõppe vormis.", self.screen, pygame.font.SysFont('Calibri', 20), (255,255,255), mx + 50, my)
            text_thing("See annab võimaluse töö ja õpingute sobitamiseks ning paindlikkuseks.", 
                       self.screen, pygame.font.SysFont('Calibri', 20), (255,255,255), mx + 50, my+ 20)
            if self.clike:
                self.score += 1
        self.counter = text_thing(str(self.score), self.screen, pygame.font.SysFont('Calibri', 60), (25,255,255), 1280 / 2, 100)
        self.clike = False

    def working(self, workers):
        seconds=(pygame.time.get_ticks()-self.tick)/1000
        if seconds >= 1:
            self.score += workers
        if seconds>=1:
         self.tick = pygame.time.get_ticks()
def game():
    pygame.init()

    screen = pygame.display.set_mode((1280,768))
    clicker = Clicker(screen)

    while clicker.running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clicker.running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicker.clike = True
        
        clicker.run()

        pygame.display.update()

    pygame.quit()
game()