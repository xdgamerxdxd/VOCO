import pygame
from sprites import *

class Destr():
    def __init__(self, state, screen):
        self.screen = screen
        self.runne = state
        self.entity()

    
    def entity(self):
        self.all = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(1280 / 2, 600)
        self.enemy = Enemy(1280 / 2, 200)
        self.projectile = Projectile( 1280 / 2, 600)
        self.enemies.add(self.enemy)
        self.bullets.add(self.projectile)
        self.all.add(self.player, self.enemy, self.projectile)

    def run(self):

        clock = pygame.time.Clock()
        while self.runne:
            k = pygame.key.get_pressed()
            self.screen.fill((0, 0, 0))
            self.player.run(pygame.K_LEFT, pygame.K_RIGHT)
            self.projectile.run(self.player.rect.x, self.player.rect.y)
            self.all.draw(self.screen)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runne = False

            pygame.display.update()
            clock.tick(60)