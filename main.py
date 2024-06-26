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

def main():
    running = True
    move = True
    boxCenter = getBoxCenter(SCREEN_WIDTH, boxSide=boxSide)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GAME XOX")
    screen.fill("white")
    turn = 0

    font = pygame.font.SysFont("freesansbold.ttf", 64)

    drawLines(screen, SCREEN_WIDTH, boxSide)
    drawNum(screen, font=font, boxs=boxCenter) 
    
    while running:
        global play
        keys = pygame.key.get_pressed()
        if (keys[K_q]):
                play = False
                running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                play = False
                running = False
            if event.type == MOUSEBUTTONDOWN and move:
                turn += clicked(screen, event.pos, boxCenter, turn)
                move = isWin(screen, boxCenter)
            if event.type == MOUSEBUTTONDOWN and not move:
                running = getTryAgain(screen, event.pos)
    

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play = True
    while(play):
        main()
    