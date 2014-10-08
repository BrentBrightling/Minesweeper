import pygame
import sys
import random
import time

# Creating the grid with rows cols and unchecked or checked
def createBoard (rows, cols):
    global grid
    grid = [[[0, 0] for j in range (0, cols)] for i in range(0,rows)]
    return grid

# drawing the board on screen
def drawBoard (rows, cols):
    global screen
    screen = pygame.display.set_mode ((cols * 30, rows * 30))
    for i in range (cols-1):
        pygame.draw.line(screen, (255,255,255), (30*(i+1),0), (30*(i+1), rows*30))
        pygame.display.update()
    for i in range (rows-1):
        pygame.draw.line(screen, (255,255,255), (0,30*(i+1)), (cols*30,30*(i+1)))
        pygame.display.update()

# Counting the number of mines
def mineCounter (rows,cols):
    for col in range (0,cols):
        for row in range (0, rows):
            mineCount = 0
            if col < cols-1:
                if grid[row][col+1][0] == -1:               # Right
                    mineCount = mineCount + 1
                if row > 0:
                    if grid[row-1][col+1][0] == -1:         # Up-Right
                        mineCount = mineCount + 1
                if row < rows-1:
                    if grid[row+1][col+1][0] == -1:         # Down-Right
                        mineCount = mineCount + 1
            if row < rows -1:                               # Down
                if grid[row+1][col][0] == -1:
                    mineCount = mineCount + 1
            if row > 0:
                if grid[row-1][col][0] == -1:               # Up
                    mineCount = mineCount +1
            if col > 0:
                if grid[row][col-1][0] == -1:               # Left
                    mineCount = mineCount + 1
                if row >0:
                    if grid[row-1][col-1][0] == -1:         # Up-Left
                        mineCount = mineCount +1
                if row < rows-1:
                    if grid[row+1][col-1][0] == -1:         # Up- Right
                        mineCount = mineCount +1
            if grid[row][col][0] != -1:                     # If there isnt a bomb there, then set the tile value to mineCount
                grid[row][col][0] = mineCount

# Display the tiles after they have been clicked
def displayTiles (locy,locx):
    box = pygame.Rect(locx*30 + 1, locy*30+1, 29, 29)
    pygame.draw.rect(screen,(255,255,255),box, 0)
    label = myfont.render(str (grid[locy][locx][0]), 1, (0,0,0))
    screen.blit(label, (locx*30+10,locy*30+10))
    pygame.display.update()

# Recursion for uncovering the tiles, does the same as mine count, but check to see if it is a 0 or a number
# if it is a number it calls itself on the square that a zero, if it's a number it just displays it
def uncoverTiles(locy,locx,rows,cols):
    if grid[locy][locx][1] == 0:
        displayTiles (locy,locx)
    if (grid[locy][locx][0] == 0) and (grid[locy][locx][1]==0):
        grid[locy][locx][1] = 1
        if locx < cols-1:
            if grid[locy][locx+1][0] == 0 and (grid[locy][locx+1][1]==0):
                uncoverTiles (locy,locx+1,rows,cols)
            elif grid[locy][locx+1][0] >0 and (grid[locy][locx+1][1]==0):
                grid[locy][locx+1][1] = 1
                displayTiles(locy, locx+1)    
            if locy > 0:
                if grid[locy-1][locx+1][0] == 0 and (grid[locy-1][locx+1][1]==0) :
                    uncoverTiles(locy-1,locx+1,rows,cols)
                elif grid[locy-1][locx+1][0] > 0 and (grid[locy-1][locx+1][1]==0):
                    displayTiles(locy-1,locx+1)
                    grid[locy-1][locx+1][1] = 1
            if locy < rows-1:
                if grid[locy+1][locx+1][0] == 0 and (grid[locy+1][locx+1][1]==0):
                    uncoverTiles (locy+1,locx+1,rows,cols)
                elif grid[locy+1][locx+1][0] > 0 and (grid[locy+1][locx+1][1]==0):
                    displayTiles(locy+1,locx+1)
                    grid[locy+1][locx+1][1] = 1
        if locy < rows -1:
            if (grid[locy+1][locx][0] == 0) and (grid[locy+1][locx][1]==0):
                uncoverTiles (locy+1,locx,rows,cols)
            elif (grid[locy+1][locx][0] > 0) and (grid[locy+1][locx][1]==0):
                grid[locy+1][locx][1] = 1
                displayTiles(locy+1,locx)
        if locy > 0:
            if grid[locy-1][locx][0] == 0 and (grid[locy-1][locx][1]==0):
                uncoverTiles (locy-1,locx,rows,cols)
            elif grid[locy-1][locx][0] > 0 and (grid[locy-1][locx][1]==0):
                displayTiles(locy-1,locx)
                grid[locy-1][locx][1] = 1
        if locx > 0:
            if grid[locy][locx-1][0] == 0 and (grid[locy][locx-1][1]==0):
                uncoverTiles (locy,locx-1,rows,cols)
            elif grid[locy][locx-1][0] >0 and (grid[locy][locx-1][1]==0):
                displayTiles (locy,locx-1)
                grid[locy][locx-1][1] = 1
            if locy >0:
                if grid[locy-1][locx-1][0] == 0 and (grid[locy-1][locx-1][1]==0):
                    uncoverTiles (locy-1,locx-1,rows,cols)
                elif grid[locy-1][locx-1][0] >0 and (grid[locy-1][locx-1][1]==0):
                    displayTiles (locy-1,locx-1)
                    grid[locy-1][locx-1][1] = 1
            if locy < rows-1:
                if grid[locy+1][locx-1][0] == 0 and (grid[locy+1][locx-1][1]==0):
                    uncoverTiles (locy+1,locx-1,rows,cols)
                elif grid[locy+1][locx-1][0] > 0 and (grid[locy+1][locx-1][1]==0):
                    displayTiles (locy+1,locx-1)
                    grid[locy+1][locx-1][1] = 1
    grid[locy][locx][1] = 1
        
    return
             
            

pygame.init ()

# Defining rows and cols and number of bombs    
rows = int (input ('Input the amount of rows: '))
cols = int (input ('Input the amount of columns: '))
numOfBombs = int (input ('Input the amount of bombs: '))
while numOfBombs < 1 or numOfBombs > rows*cols -5:
    numOfBombs = int (input ('Input the amount of bombs: '))
numOfFlags = numOfBombs
uncovered = 0
click = 0
# making the board
grid = createBoard (rows, cols)

# Drawing the board and setting the bombs in random locations
drawBoard (rows, cols)
#print (grid)

myfont = pygame.font.SysFont("monospace", 15)
myfont2 = pygame.font.SysFont("aharoni", 30)
                
      
# Checking for mous click, if it his a mine, it draws a red box, if it hits a number or a 0 then it uncovers it using recursion
x = 0
while x == 0:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button1, button2, button3 = pygame.mouse.get_pressed()
            locx = int(mx/30)
            locy = int (my/30)
            # Making it so you can never hit a bomb on the first click
            if ((button1 ==1) or (button3 ==1)) and click == 0:
                for i in range (0,numOfBombs):
                    row = random.randint (0,rows-1)
                    col = random.randint (0,cols-1)
                    while grid[row][col][0] != 0 or row == locy and col == locx:
                        row = random.randint (0,rows-1)
                        col = random.randint (0,cols-1)    
                    grid[row][col][0] = -1
                mineCounter (rows,cols)
                click = 5
                time1 = time.clock()
            # If button is left click and its not flagged and its a mine then exit
            if button1 == 1:
                if grid[locy][locx][1] != 2:
                    if grid[locy][locx][0] == -1:
                        box = pygame.Rect(locx*30 + 1, locy*30+1, 29, 29)
                        pygame.draw.rect(screen,(255,0,0),box, 0)
                        pygame.display.update()
                        # Uncovering the rest of the mines when you lose
                        for i in range (0,cols):
                            for u in range (0,rows):
                                if grid[u][i][0] == -1:
                                    time.sleep (.3)
                                    box = pygame.Rect(i*30 + 1, u*30+1, 29, 29)
                                    pygame.draw.rect(screen,(255,0,0),box, 0)
                                    pygame.display.update()
                        time.sleep (1)
                        box = pygame.Rect(0, 0, cols*30, rows*30)
                        pygame.draw.rect(screen,(0,0,0),box, 0)
                        label = myfont2.render('You lose', 20, (255,0,0))
                        screen.blit(label, (rows/2*30 - rows/4*50, cols/2*30))
                        pygame.display.update()
                        x = 1
                        exit
                    else:
                        #if it's not a bomb then uncover it and see if all tiles have been uncovered
                        uncoverTiles(locy,locx,rows,cols)
                        uncovered = 0
                        for i in range (0,cols):
                            for u in range (0,rows):
                                if grid[u][i][0] >= 0 and grid[u][i][1] == 1:
                                    uncovered = uncovered + 1
                        print (uncovered)
                        if uncovered >= rows*cols - numOfBombs:
                            box = pygame.Rect(0, 0, cols*30, rows*30)
                            pygame.draw.rect(screen,(255,255,255),box, 0)
                            label = myfont2.render('You win', 20, (0,0,0))
                            screen.blit(label, (rows/2*30 - rows/3*30, cols/2*30))
                            pygame.display.update()
                            x=1
                            
            # If the right mouse button is clicked and the tile hasnt been uncovered than flag it
            elif button3 == 1:
                if numOfFlags > 0 and grid[locy][locx][1] == 0:
                    grid[locy][locx][1] = 2
                    numOfFlags = numOfFlags -1
                    box = pygame.Rect(locx*30 + 10, locy*30+5, 10, 10)
                    pygame.draw.rect(screen,(255,0,0),box, 0)
                    pygame.draw.line(screen,(255,0,0),(locx*30+19,locy*30+15),(locx*30+19,locy*30+25), 1)
                    pygame.display.update()
                # If it has a flag already unflag it
                elif grid[locy][locx][1] == 2:
                    grid[locy][locx][1] = 0
                    numOfFlags = numOfFlags +1
                    box = pygame.Rect(locx*30 + 10, locy*30+5, 10, 10)
                    pygame.draw.rect(screen,(0,0,0),box, 0)
                    pygame.draw.line(screen,(0,0,0),(locx*30+19,locy*30+15),(locx*30+19,locy*30+25), 1)
                    pygame.display.update()
# time and exit
time2 = time.clock()
label = myfont2.render('Time: ' +str(round((time2-time1),2))+'s', 20, (0,0,0))
screen.blit(label, (rows/2*30 - rows/3*30, cols/2*30+ 30))
pygame.display.update()
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()           
