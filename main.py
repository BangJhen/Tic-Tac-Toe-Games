from config import *
import numpy as np
import pygame
from pygame.locals import *

SCREEN_WIDTH = 666 
SCREEN_HEIGHT = 666 

# Color
WHITE = [255, 255, 255]

# Position
boxSide = 666 // 3
boxCenter = np.empty((3,3), dtype=object)
for y, posY in enumerate(range(boxSide, SCREEN_HEIGHT + 1, boxSide)):
    for x, posX in enumerate(range(boxSide,SCREEN_WIDTH + 1, boxSide)):
        boxCenter[y,x] = np.array([posX - (boxSide // 2), posY - (boxSide // 2), ""])


def main():
    running = True
    move = True
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GAME XOX")
    screen.fill("white")
    turn = 0

    font = pygame.font.SysFont("freesansbold.ttf", 64)

    drawLines(screen, SCREEN_WIDTH, boxSide)
    drawNum(screen, font=font, boxs=boxCenter) 
    while running:
        keys = pygame.key.get_pressed()
        if (keys[K_q]):
                running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN and move:
                turn += clicked(screen, event.pos, boxCenter, turn)

        # move = isWin(boxCenter, move)

        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()