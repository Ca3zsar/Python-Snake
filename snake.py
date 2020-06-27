import pygame
import random
import sys
from pygame.locals import *

# Directions.
STOP = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
directions = [STOP,LEFT,RIGHT,UP,DOWN]

# Dimensions.
WIDTH = 600
HEIGHT = 600

# COLORS
BLACK = (0,0,0)
GREEN = (0,126,0)
WHITE = (255,255,255)

# Initialize the window.
pygame.init()
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption("Snake")

mainFont = pygame.font.SysFont(None,30)

# The snake class.
class Snake(pygame.sprite.Sprite):
    def __init__(self, startX, startY, surface):
        super.__init__()
        self.bodyX = [startX]
        self.bodY = [startY]
        self.length = 1
        self.dir = STOP

def terminate():
    pygame.quit()
    sys.exit()

def waitForKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

def drawText(text, x, y,font):
    textobj = font.render(text, 1, GREEN)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    windowSurface.blit(textobj, textrect)

def Draw():
    windowSurface.fill(BLACK)
    


def main():
    while True:
        # Draw the "main menu" text and wait for user's input to continue or exit.
        windowSurface.fill(BLACK)
        drawText("Press enter to continue",WIDTH/2,HEIGHT/2,mainFont)
        pygame.display.update()
        
main()