import pygame

global i
i = 'images/'

class Test(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Test, self).__init__()

        self.image = pygame.image.load(f'{i}Test.png')
        self.rect = self.image.get_rect()
        self.rect.centery = y / 2
        self.rect.centerx = x / 2
    
    def run(self):
        global mx, my
        mx, my = pygame.mouse.get_pos()
        self.image = pygame.image.load(f'{i}Test.png')

        if self.rect.collidepoint((mx, my)):
            self.image = pygame.image.load(f'{i}Teste.png')

class Worker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Worker, self).__init__()

        self.image = pygame.image.load(f'{i}student.png')
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x / 2
        self.count = 0
    
    def run(self):
        self.image = pygame.image.load(f'{i}student.png')

        if self.rect.collidepoint((mx, my)):
            self.image = pygame.image.load(f'{i}student selected.png')

class Farm_worker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Farm_worker, self).__init__()

        self.image = pygame.image.load(f'{i}farm worker.png')
        self.rect = self.image.get_rect()

        self.rect.y = y 
        self.rect.x = x / 2
        self.count = 0
    
    def run(self):
        self.image = pygame.image.load(f'{i}farm worker.png')

        if self.rect.collidepoint((mx, my)):
            self.image = pygame.image.load(f'{i}farm worker selected.png')

class Hard_worker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Hard_worker, self).__init__()

        self.image = pygame.image.load(f'{i}hard worker.png')
        self.rect = self.image.get_rect()

        self.rect.y = y 
        self.rect.x = x / 2
        self.count = 0
    
    def run(self):
        self.image = pygame.image.load(f'{i}hard worker.png')

        if self.rect.collidepoint((mx, my)):
            self.image = pygame.image.load(f'{i}hard worker selected.png')