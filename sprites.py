import pygame
import random

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

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.image.load(f'{i}controla.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self, left, right):
        k = pygame.key.get_pressed()
        if k[left] and self.rect.x > 0:
            self.rect.x -= 1
        if k[right] and self.rect.x < 1280 - self.rect.width:
            self.rect.x += 1

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Projectile, self).__init__()

        self.image = pygame.image.load(f'{i}nowepon.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tick = pygame.time.get_ticks()
        self.seconds = (pygame.time.get_ticks() - self.tick) / 1000


    def run(self, x, y):
        k = pygame.key.get_pressed()
        self.image = pygame.image.load(f'{i}nowepon.png')
        self.rect = self.image.get_rect()
        print(self.seconds)
        if k[pygame.K_z] and self.seconds <= 3:
            self.time = True
            self.image = pygame.image.load(f'{i}projectile.png')
            self.rect = self.image.get_rect()
            self.rect.x = x + 30
            self.rect.y = y - 600
        self.seconds = (pygame.time.get_ticks() - self.tick) / 1000
        if k[pygame.K_z] and self.seconds >= 10:
                self.tick = pygame.time.get_ticks()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  

        self.image = pygame.image.load(f'{i}angy controla.png')  
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.health = 1000
        self.tick = pygame.time.get_ticks()
        self.int = 5

    def run(self):
        self.seconds = (pygame.time.get_ticks() - self.tick) / 1000
        if self.health < 1000:
            if self.seconds >= 2:
                self.int = random.randint(1, 10)
            if self.int > 5 and self.rect.x > 0:
                self.rect.x -= 4
            elif self.int <= 5 and self.rect.x < 1280 - self.rect.width:
                self.rect.x += 4
        if self.seconds >= 2:
            self.tick = pygame.time.get_ticks()

class Voco_uks(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super(Voco_uks, self).__init__()
        self.image = pygame.image.load(f'{i}voco_uksed.png')  
        self.image = pygame.transform.scale(self.image, (1280, 768))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def run(self):
        pass
 
class Voco_fuajee(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super(Voco_fuajee, self).__init__()
        self.image = pygame.image.load(f'{i}asendus fuajee.png')
        self.image = pygame.transform.scale(self.image, (1280, 768))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
    
class Voco_korridor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_korridor, self).__init__()  

        self.image = pygame.image.load(f'{i}korridor.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_trepp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_trepp, self).__init__()  

        self.image = pygame.image.load(f'{i}trepp.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_trepp2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_trepp2, self).__init__()  

        self.image = pygame.image.load(f'{i}trepp 2.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_trep3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_trep3, self).__init__()  

        self.image = pygame.image.load(f'{i}trep 3.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_3korrus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_3korrus, self).__init__()  

        self.image = pygame.image.load(f'{i}3korrus koridor.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_klass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_klass, self).__init__()  

        self.image = pygame.image.load(f'{i}klass.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_joonas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_joonas, self).__init__()  

        self.image = pygame.image.load(f'{i}joonas pilves.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
class Voco_margus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Voco_margus, self).__init__()  

        self.image = pygame.image.load(f'{i}margus jumpscare.png') 
        self.image = pygame.transform.scale(self.image, (1280, 768)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self):
        pass
            
