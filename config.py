import pygame

# Lines
def drawLines(surface, screen_max : int, boxArea : int) -> None:
    for i in range(0, screen_max + 1, boxArea): 
        pygame.draw.line(surface, "black", (0, i), (screen_max, i), 6)
        pygame.draw.line(surface, "black", (i, 0), (i, screen_max), 6)

# Draw X
def drawX(surface, box : list) -> None:
    pygame.draw.line(surface, "black", (box[0] - 70, box[1] + 70), (box[0] + 70, box[1] - 70), 8)
    pygame.draw.line(surface, "black", (box[0] - 70, box[1] - 70), (box[0] + 70, box[1] + 70), 8)

# Draw Circle (O)
def drawO(surface, box : list[int, int]) -> None:
    pygame.draw.circle(surface, "black", (box[0] , box[1] ), 90, 5)
    
# Draw Number
def drawNum(surface, font, boxs : dict) -> None:
    for i, box in enumerate(boxs):
        text = font.render(str(i + 1), True, pygame.Color(0,0,0,128))
        textRect = text.get_rect()
        textRect.center = (box[0], box[1])
        
        surface.blit(text, textRect)
        
def clicked(surface ,pos : list, boxAreas : dict, player):
    for key, value in (boxAreas.items()):
        if (value == "X" or value == "O"):
            continue
        boxAxis = key[0]
        boxOrd = key[1]
        
        posAxis = pos[0]
        posOrd = pos[1]
        if (posAxis > (boxAxis - 111) and posAxis < (boxAxis + 111)) and (posOrd > (boxOrd - 111) and posOrd < (boxOrd + 111)):
            if (player % 2 == 0):
                drawO(surface=surface, box=key)
                boxAreas[key] = "O"
            elif (player % 2 == 1):
                drawX(surface=surface, box=key)
                boxAreas[key] = "X"
            return 1
    return 0

def isWin(boxAreas : dict, move):
    if not move:
        return False
    boxValueList = [boxArea for boxArea in boxAreas.values()]
    
    for rows in range(0, 3):
        if (boxValueList[rows] == boxValueList[rows + 3] == boxValueList[rows + 6] == "O"):
            print(f"O Was Win")
            return False
        if (boxValueList[rows] == boxValueList[rows + 3] == boxValueList[rows + 6] == "X"):
            print(f"X Was Win")
            return False
    for cols in range(0, 7, 3):
        if (boxValueList[cols] == boxValueList[cols + 1] == boxValueList[cols + 2] == "O"):
            print(f"Player O Was Win")
            return False
        elif (boxValueList[cols] == boxValueList[cols + 1] == boxValueList[cols + 2] == "X"):
            print(f"Player X Was Win")
            return False
        
    if (boxValueList[0] == boxValueList[4] == boxValueList[8] == "O"):
        print(f"O Was Win")
        return False
    elif (boxValueList[0] == boxValueList[4] == boxValueList[8] == "X"):
        print(f"X Was Win")
        return False
    elif (boxValueList[2] == boxValueList[4] == boxValueList[6] == "O"):
        print(f"O Was Win")
        return False
    elif (boxValueList[2] == boxValueList[4] == boxValueList[6] == "X"):
        print(f"X Was Win")
        return False
    return True