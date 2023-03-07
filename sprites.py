import pygame

class Test(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Test, self).__init__()

        self.image = pygame.image.load('images/Test.png')
        self.rect = self.image.get_rect()
        self.rect.centery = y / 2
        self.rect.centerx = x / 2
    
    def run(self):
        mx, my = pygame.mouse.get_pos()
        self.image = pygame.image.load('images/Test.png')

        if self.rect.collidepoint((mx, my)):
            self.image = pygame.image.load('images/Teste.png')

class Worker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Worker, self).__init__()

        self.image = pygame.image.load('images/child.png')
        self.rect = self.image.get_rect()
        self.rect.y = y / 2
        self.rect.x = x / 2
        self.count = 0
    
    def run(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint((mx, my)):
            pass
            