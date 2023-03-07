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
    def __init__(self, screen, state):
        self.screen = screen
        self.running = state
        self.entities()
        self.score = 0
        self.highest_score = 0
        # How many bought
        self.workers = 0
        self.farmers = 0
        self.hworkers = 0
        # Starting price
        self.ammount = 50
        self.fammount = 1000
        self.hammount = 10000
        self.tick = pygame.time.get_ticks()
        self.seconds = (pygame.time.get_ticks() - self.tick) / 1000
        pygame.display.set_caption("Clicker gamer")
        global font
        font = pygame.font.SysFont('Calibri', 20)

    def entities(self):
        self.all = pygame.sprite.Group()
        self.worker = Worker(200, 100)
        self.farmer = Farm_worker(200, 300)
        self.hworker = Hard_worker(200, 500)
        self.test = Test(1280, 768)
        self.all.add(self.test, self.worker, self.farmer, self.hworker)

    def run(self):
        clike = False
        while self.running:
            self.screen.blit(pygame.image.load(f'{i}clickerground.png'), (0, 0))
            mx, my = pygame.mouse.get_pos()
            self.all.draw(self.screen)
            self.test.run()
            self.worker.run()
            self.farmer.run()
            self.hworker.run()
            self.working(self.workers)
            self.farming(self.farmers)
            self.hworking(self.hworkers)

            # Prices
            student = text_thing(str(self.ammount), self.screen, pygame.font.SysFont('Calibri', 50), (255, 255, 255), 200, 200)
            farmer = text_thing(str(self.fammount), self.screen, pygame.font.SysFont('Calibri', 50), (255, 255, 255), 230, 360)
            hworker = text_thing(str(self.hammount), self.screen, pygame.font.SysFont('Calibri', 50), (255, 255, 255), 240, 580)

            self.seconds = (pygame.time.get_ticks() - self.tick) / 1000
            if self.seconds>=1:
                self.tick = pygame.time.get_ticks()

            # Buying
            if self.worker.rect.collidepoint((mx, my)):
                text_thing('VOCOs on kokku 75 kursust', self.screen, font, (255,255,255), mx + 50, my)
                if clike and self.score >= self.ammount:
                    self.workers += 1
                    self.score -= self.ammount
                    self.ammount += 3
            if self.farmer.rect.collidepoint((mx, my)):
                text_thing('VOCO pakub 14 tasuta kursust', self.screen, font, (255, 255, 255), mx + 50, my)
                if clike and self.score >= self.fammount:
                    self.farmers += 1
                    self.score -= self.fammount
                    self.fammount += 2000
            if self.hworker.rect.collidepoint((mx, my)):
                text_thing('Õppekava on välja töötatud koostöös ettevõtetega', self.screen, font, (255, 255, 255), mx + 100, my)
                text_thing('ning õppetöö sisaldab palju praktilisi ülesandeid ja projekte.', 
                           self.screen, font, (255, 255, 255), mx + 100, my + 20)
                if clike and self.score >= self.hammount:
                    self.hworkers += 1
                    self.score -= self.hammount
                    self.hammount += 5000


            if self.test.rect.collidepoint((mx, my)):
                text_thing("Õppetöö toimub nii päeva- kui kaugõppe vormis.", self.screen, font, (255,255,255), mx + 50, my)
                text_thing("See annab võimaluse töö ja õpingute sobitamiseks ning paindlikkuseks.", 
                        self.screen, font, (255,255,255), mx + 50, my + 20)
                if clike:
                    self.score += 1

            if self.highest_score < self.score:
                self.highest_score = self.score
            self.counter = text_thing(str(self.score), self.screen, pygame.font.SysFont('Calibri', 60), (25,255,255), 1280 / 2, 100)
            clike = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clike = True
                    if event.button == 0:
                        clike = True
            pygame.display.update()
        

    def working(self, workers):
        if self.seconds >= 1:
            self.score += workers * 2

    def farming(self, farmers):
        if self.seconds >= 1:
            self.score += farmers * 50

    def hworking(self, hworkers):
        if self.seconds >= 1:
            self.score += hworkers * 1000