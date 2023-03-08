import pygame
from sprites import *
from clicker import text_thing

class Destr():
    # algus intid
    def __init__(self, state, screen):
        self.screen = screen
        self.runne = state
        self.points = 0
        self.entity()

    # tegelased
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
            text = text_thing(str(self.enemy.health), self.screen, pygame.font.SysFont('Calibri', 50), (255, 0, 0), self.enemy.rect.x + 200, self.enemy.rect.y + 300)
            self.player.run(pygame.K_LEFT, pygame.K_RIGHT)
            self.enemy.run()
            self.projectile.run(self.player.rect.x, self.player.rect.y)
            self.all.draw(self.screen)

            if pygame.sprite.spritecollideany(self.enemy, self.bullets):
                self.enemy.health -= 100
            if self.enemy.health <= 0:
                self.enemy.kill()
                self.points += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runne = False

            pygame.display.update()
            clock.tick(60)