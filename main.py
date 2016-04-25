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

FPS = .5 
FPSCLOCK = pygame.time.Clock()
DISPWIDTH = 100
DISPHEIGHT = 100
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

if len(sys.argv) > 1:
  level_file = sys.argv[1]
else:
  level_file = "./glider.txt"

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

  def loadFile(self, fileName):
    self.text = [row.strip('\n') for row in\
      open(fileName, 'r').readlines()]
    for line in self.text:
      if len(line) > self.levelWidth:
        self.levelWidth = len(line)
    self.levelHeight = len(self.text)
   
  def loadCells(self):
    dispCenterX = DISPWIDTH / 2
    dispCenterY = DISPWIDTH / 2
    levelCenterX = self.levelWidth / 2
    levelCenterY = self.levelHeight / 2
    startLeftX = dispCenterX - levelCenterX
    startTopY = dispCenterY - levelCenterY
     
    y = startTopY 
    for row in self.text:
      x = startLeftX
      for letter in row:
        if letter != ' ':
          allCells.add(Cell(x, y))
        x += 1
      y += 1 
      
##################################################
#Build a player class to control ptb as we play.
##################################################
class Cell(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super(Cell, self).__init__()
    self.image = pygame.Surface([1, 1])
    self.image.fill(BLACK)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.nebList = []
    self.deadNebList = []
    self.liveNebs = 0
    
    for i in (self.rect.x - 1, self.rect.x, self.rect.x +1):
      for j in (self.rect.y -1, self.rect.y, self.rect.y +1):
        if (i, j) == (self.rect.x, self.rect.y):
          next
        else:
          self.nebList.append((i, j))
    
  def update(self):
    self.liveNebs = 0
    self.deadNebList = list(self.nebList)
    for x, y in self.nebList:
      for cell in allCells:
        if (x, y) == (cell.rect.x, cell.rect.y):
          self.liveNebs += 1
          self.deadNebList.remove((x, y))
    if (self.liveNebs > 3) or (self.liveNebs < 2):
      killList.append(self)
      
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
allCells = pygame.sprite.Group()

################################################
#Load a Level File
################################################
workingLevel = Level()
workingLevel.loadFile(level_file)
workingLevel.loadCells()

################################################
#  Start the game loop!!!!!!!!
################################################
while True:
  for event in pygame.event.get():
    if event.type == QUIT or keyPressed(K_ESCAPE):
      pygame.quit()
      sys.exit()
  
  DISPSURF.fill(WHITE)
  allCells.draw(DISPSURF)
  pygame.display.update()
  pygame.display.flip()

 
  nebCount = collections.Counter({})
  bornList = []
  killList = []

  allCells.update()
  
  for cell in allCells:
    nebCount += collections.Counter(cell.deadNebList)
  
  for (x, y) in nebCount:
    if nebCount[(x, y)] > 2:
      bornList.append(Cell(x, y))

  allCells.add(bornList)
  
  allCells.remove(killList)
  print "k", len(killList), "b", len(bornList), "Tot", len(allCells)


  FPSCLOCK.tick(FPS)
