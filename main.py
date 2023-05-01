import pygame
from settings import 


class Game:

    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pygame Template')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.WIN.fill(WHITE)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
