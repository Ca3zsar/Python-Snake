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
mainClock = pygame.time.Clock()

mainFont = pygame.font.SysFont(None,30)

# The snake class.
class Snake(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        super().__init__()
        self.bodyX = [startX]
        self.bodyY = [startY]
        self.length = 1
        self.dir = STOP
    def draw(self):
        for i in range(self.length):
            bodyRect = pygame.Rect(self.bodyX[i],self.bodyY[i],20,20)
            pygame.draw.rect(windowSurface,GREEN,bodyRect)
            

def terminate():
    pygame.quit()
    sys.exit()

def waitForKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return
                if event.key == K_ESCAPE:
                    terminate()
    

def drawText(text, x, y,font):
    textobj = font.render(text, 1, GREEN)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    windowSurface.blit(textobj, textrect)

def Draw(snake):
    windowSurface.fill(BLACK)
    #Draw the borders of the game:
    pygame.draw.line(windowSurface,WHITE,(50,50),(50,550))
    pygame.draw.line(windowSurface,WHITE,(550,50),(550,550))
    pygame.draw.line(windowSurface,WHITE,(50,50),(550,50))
    pygame.draw.line(windowSurface,WHITE,(50,550),(550,550))
    
    #Draw the snake.
    snake.draw()
    
    #Draw the score.
    drawText(f"Score : {snake.length}",WIDTH//2,575,mainFont)
    
    pygame.display.update()
    

def Input(snake):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                snake.dir = UP
                break
            if event.key == K_DOWN or event.key == K_s:
                snake.dir = DOWN
                break
            if event.key == K_LEFT or event.key == K_a:
                snake.dir = LEFT
                break
            if event.key == K_RIGHT or event.key == K_d:
                snake.dir = RIGHT
                break
            if event.key == K_ESCAPE:
                terminate()
        if event.type == QUIT:
            terminate()

def main():
    while True:
        # Initialize the snake.
        snake = Snake(WIDTH//2+10,HEIGHT//2+10)
        # Draw the "main menu" text and wait for user's input to continue or exit.
        windowSurface.fill(BLACK)
        drawText("Press enter to continue",WIDTH//2,HEIGHT//2,mainFont)
        pygame.display.update()
        waitForKey()
        while True:
            Draw(snake)
            Input(snake)
            
        
main()