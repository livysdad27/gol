#!/usr/bin/python
##########################
#Name:  main.py
#Author:  Billy Jackson
#Purpose: Test my weird Conway's Game of Life Algorithm
#Date:  04/23/16
##########################
import pygame, sys, time, collections
from pygame.locals import *
from pygame import gfxdraw

# Set some globals.  FPS is the speed in frames per second
FPS = 1 
FPSCLOCK = pygame.time.Clock()
CELLWIDTH = 1 
CELLHEIGHT = 1 
DISPWIDTH = 500
DISPHEIGHT = 500
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

#Get a text file with a pattern in it.
if len(sys.argv) > 1:
  level_file = sys.argv[1]
else:
  level_file = "./glider.txt"

if len(sys.argv) > 2:
  FPS = float(sys.argv[2])

if len(sys.argv) > 3:
  CELLWIDTH = float(sys.argv[3])
  CELLHEIGHT = CELLWIDTH

#Initialize pygame and setup the display
pygame.init

DISPSURF = pygame.display.set_mode((DISPWIDTH, DISPHEIGHT))
pygame.display.set_caption("GOL Prototype")

##################################################
# Level class for loading new patterns of cells
##################################################
class Level(object):
  def __init__(self):
    self.levelHeight = 0
    self.levelWidth = 0
    self.text = []

  #Get a file and measure it to set the level height/width.
  #  Also read it into self.text.
  def loadFile(self, fileName):
    self.text = [row.strip('\n') for row in\
      open(fileName, 'r').readlines()]
    for line in self.text:
      if len(line) > self.levelWidth:
        self.levelWidth = len(line)
    self.levelHeight = len(self.text)

  #Find the center of the display and set the starting
  #  X/Y of the pattern 
  def loadCells(self):
    dispCenterX = (DISPWIDTH / 2) / CELLWIDTH
    dispCenterY = (DISPHEIGHT / 2) / CELLHEIGHT
    levelCenterX = self.levelWidth / 2
    levelCenterY = self.levelHeight / 2
    startLeftX = dispCenterX - levelCenterX
    startTopY = dispCenterY - levelCenterY
     
    #Read in the pattern file and any character that
    #  isn't a space becomes a live cell
    y = startTopY 
    for row in self.text:
      x = startLeftX
      for letter in row:
        if letter != ' ':
          allCells.append((x, y))
        x += 1
      y += 1 
      
##################################################
#Build a player class to control ptb as we play.
##################################################
    #Scan for your neighbors, dead or alive.  Prolly faster
    #  just as a bunch of static calcs.  Put your neighbors
    # in a list for use scanning for alive stuff.

def countNbrs((x, y)):
  liveNbrCount = 0
  nbrList = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), \
             (x - 1, y),                 (x + 1, y),     \
             (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
  for cell in allCells:
    for nbr in nbrList:
      if nbr == cell:
        liveNbrCount += 1
        nbrList.remove(cell)
  return liveNbrCount, nbrList     

################################################
#Simple utility function to get if a key has been pressed on the keyboard
################################################
def keyPressed(key):
  keysPressed = pygame.key.get_pressed()
  if keysPressed[key]:
    return True
  else:
    return False 

################################################
#Create an all sprites list
################################################
#Sprtegroup to keep the working list of live cells
allCells = []

################################################
#Load a Level File
################################################
#Load a pattern file
workingLevel = Level()
workingLevel.loadFile(level_file)
workingLevel.loadCells()

################################################
#  Start the game loop!!!!!!!!
################################################
generation = 0
while True:
  #See if we're trying to quit (weird at slow framerates)
  for event in pygame.event.get():
    if event.type == QUIT or keyPressed(K_ESCAPE):
      pygame.quit()
      sys.exit()
  

  print generation
  #Set an all whit esurface, draw all the cells, handle display
  DISPSURF.fill(WHITE)

  for x, y in allCells:
    DISPSURF.fill(BLACK, (x * CELLWIDTH, y * CELLHEIGHT, CELLWIDTH, CELLHEIGHT))


  #allCells.draw(DISPSURF)
  pygame.display.update()
  pygame.display.flip()

  #Do Housekeeping on the bornList, killList and nebCount.
  #  nebCount is a colleection counter object that then spits
  #  out a key value pair where the value is the number of occurances
  #  of key.  The key is the coordinates of dead neighbor cells.  If 
  #  any dead neighbor cell shows up 3 or more times it's a new cell
  #  and gets appended to the born list. 
  deadNbrCount = collections.Counter({})
  killList = []
  bornList = []

  #Run the update method on all cells.
  for cell in allCells:
    living, dead = countNbrs(cell)
    if (living > 3) or (living < 2):
      killList.append(cell)
    deadNbrCount += collections.Counter(dead)


  #Detect deadNebList entries that occur more than twice and append those
  #  To the bornlist
  for (x, y) in deadNbrCount:
    if deadNbrCount[(x, y)] == 3:
      bornList.append((x, y))

  #Remove cells in the killList from allCells
  #allCells.remove(killList)
  allCells = [z for z in allCells if z not in killList]
  allCells += bornList

  generation += 1
  #Print housekeeping
  #print "k", len(killList), "Tot", len(allCells)

  #Ticke the clock
  FPSCLOCK.tick(FPS)
