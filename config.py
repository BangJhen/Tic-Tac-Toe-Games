import pygame
import numpy as np

# Lines
def drawLines(surface, screen_max : int, boxArea : int) -> None:
    for i in range(0, screen_max + 1, boxArea): 
        pygame.draw.line(surface, "black", (0, i), (screen_max, i), 6)
        pygame.draw.line(surface, "black", (i, 0), (i, screen_max), 6)

# Draw X
def drawX(surface, box) -> None:
    boxAxis = int(box[0])
    boxOrd = int(box[1])
    pygame.draw.line(surface, "black", (boxAxis - 70, boxOrd + 70), (boxAxis + 70, boxOrd - 70), 8)
    pygame.draw.line(surface, "black", (boxAxis - 70, boxOrd - 70), (boxAxis + 70, boxOrd + 70), 8)

# Draw Circle (O)
def drawO(surface, box) -> None:
    boxAxis = int(box[0])
    boxOrd = int(box[1])
    pygame.draw.circle(surface, "black", (boxAxis , boxOrd), 90, 5)
    
# Draw Number
def drawNum(surface, font, boxs) -> None:
    nums = 1
    for rows in (boxs):
        for cols in (rows):
            text = font.render(str(nums), True, pygame.Color(0,0,0,128))
            textRect = text.get_rect()
            textRect.center = (int(cols[0]), int(cols[1]))
            
            surface.blit(text, textRect)
            nums += 1
    
def clicked(surface ,pos : list, boxAreas : object, player):
    for rows in boxAreas:
        for cols in rows:
            value = cols[2]
            if (value == "X" or value == "O"):
                continue
            boxAxis = int(cols[0])
            boxOrd = int(cols[1])
            
            posAxis = pos[0]
            posOrd = pos[1]
            if (posAxis > (boxAxis - 111) and posAxis < (boxAxis + 111)) and (posOrd > (boxOrd - 111) and posOrd < (boxOrd + 111)):
                if (player % 2 == 0):
                    drawO(surface=surface, box=cols)
                    cols[2] = "O"
                elif (player % 2 == 1):
                    drawX(surface=surface, box=cols)
                    cols[2] = "X"
                return 1
    return 0

def isWin(boxAreas : dict, move):
    if not move:
        return False
    boxValueList = [boxArea for boxArea in boxAreas.values()]
    
    for rows in range(0, 3):
        if (boxValueList[rows] == boxValueList[rows + 3] == boxValueList[rows + 6] == "O"):
            print(f"Player O Was Win")
            return False
        if (boxValueList[rows] == boxValueList[rows + 3] == boxValueList[rows + 6] == "X"):
            print(f"Player X Was Win")
            return False
    for cols in range(0, 7, 3):
        if (boxValueList[cols] == boxValueList[cols + 1] == boxValueList[cols + 2] == "O"):
            print(f"Player O Was Win")
            return False
        elif (boxValueList[cols] == boxValueList[cols + 1] == boxValueList[cols + 2] == "X"):
            print(f"Player X Was Win")
            return False
        
    if (boxValueList[0] == boxValueList[4] == boxValueList[8] == "O"):
        print(f"Player O Was Win")
        return False
    elif (boxValueList[0] == boxValueList[4] == boxValueList[8] == "X"):
        print(f"Player X Was Win")
        return False
    elif (boxValueList[2] == boxValueList[4] == boxValueList[6] == "O"):
        print(f"Player O Was Win")
        return False
    elif (boxValueList[2] == boxValueList[4] == boxValueList[6] == "X"):
        print(f"Player X Was Win")
        return False
    return True