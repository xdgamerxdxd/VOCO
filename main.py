import pygame
from menu import Main_menu, screen_height, screen_width

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
    
    def run(self):
        self.main_menu()

    def main_menu(self):
        main = Main_menu(self.screen)
        main.run()


def main():

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
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