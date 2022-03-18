import pygame, sys
from pygame import QUIT

pygame.init()

def main():

    DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption("The Legend of Adlez")

    birdImg = pygame.image.load("resources/bird.png");
    birdx = 10
    birdy = 10
    direction = 'right'

    while True:
        # DISPLAYSURF.fill(pygame.color.WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        DISPLAYSURF.blit(birdImg, (birdx, birdy))
        pygame.display.update()


if __name__ == '__main__':
    main()
