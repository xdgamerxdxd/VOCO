import pygame
#from clicker import *

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
    
    def run(self):
        pass

def main():

    pygame.init()

    screen = pygame.display.set_mode((1280,768))
    game = Game(screen)
    clock = pygame.time.Clock()

    while game.running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        game.run()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
main()
