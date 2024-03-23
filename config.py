import pygame
import numpy as np

# BoxCenter
def getBoxCenter(screen_max : int, boxSide : int):
    boxCenter = np.empty((3,3), dtype=object)
    for y, posY in enumerate(range(boxSide, screen_max + 1, boxSide)):
        for x, posX in enumerate(range(boxSide,screen_max + 1, boxSide)):
            boxCenter[y,x] = np.array([posX - (boxSide // 2), posY - (boxSide // 2), ""])

    return boxCenter

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
            text = font.render(str(nums), True, "black")
            textRect = text.get_rect()
            textRect.center = (int(cols[0]), int(cols[1]))
            
            surface.blit(text, textRect)
            nums += 1
    
def clicked(surface ,pos : list, boxAreas : object, player) -> int:
    for rows in boxAreas:
        for cols in rows:
            value = cols[2]
            boxAxis = int(cols[0])
            boxOrd = int(cols[1])
            if (value == "X" or value == "O"):
                continue
            
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

def isWin(surface, boxAreas : object) -> bool:
    for rows in boxAreas:
        if (rows[0][2] == rows[1][2] == rows[2][2] == "O"):
            playerWin(surface=surface, player="O")
            return False
        elif (rows[0][2] == rows[1][2] == rows[2][2] == "X"):
            playerWin(surface=surface, player="X")
            return False
        
    for cols in boxAreas.T:
        if (cols[0][2] == cols[1][2] == cols[2][2] == "O"):
            playerWin(surface=surface, player="O")
            
            return False
        elif (cols[0][2] == cols[1][2] == cols[2][2] == "X"):
            playerWin(surface=surface, player="X")            
            return False
    
    if (boxAreas[0][0][2] == boxAreas[1][1][2] == boxAreas[2][2][2] == "O"):
        playerWin(surface=surface, player="O")        
        return False
    elif (boxAreas[0][0][2] == boxAreas[1][1][2] == boxAreas[2][2][2] == "X"):
        playerWin(surface=surface, player="X")        
        return False
    if (boxAreas[0][2][2] == boxAreas[1][1][2] == boxAreas[2][0][2] == "O"):
        playerWin(surface=surface, player="O")
        return False
    elif (boxAreas[0][2][2] == boxAreas[1][1][2] == boxAreas[2][0][2] == "X"):
        playerWin(surface=surface, player="X")
        return False
    
    return True

def playerWin(surface, player : str) -> None:
    font = pygame.font.SysFont("freesansbold.ttf", 128)
    text = font.render(f"Player {player} WIN", True, "red")
    textRect = text.get_rect()
    textRect.center = (666//2 , 666//2)
    
    surface.blit(text, textRect)
    
def getTryAgain(surface ,pos : list):
    center = 222
    font = pygame.font.SysFont("freesansbold.ttf", 64)
    
    pygame.draw.rect(surface=surface, color="red", rect=(center - 50, center + 200, center + 100, 150))
    surface.blit(font.render(f"TRY AGAIN", True, "white"), (center - 12, center + 255))
    
    posAxis = pos[0]
    posOrd = pos[1]
    if ((posAxis >= 175 and posAxis <= 495) and (posOrd >= 425 and posOrd <= 570)):
        return False
    return True
        
    