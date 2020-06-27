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

# The food class.
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        foodRect = pygame.Rect(self.x+5,self.y+5,10,10)
        pygame.draw.rect(windowSurface,WHITE,foodRect)

# The snake class.
class Snake(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        super().__init__()
        self.headX = startX
        self.headY = startY
        self.bodyX = [startX]
        self.bodyY = [startY]
        self.length = 1
        self.dir = UP
    def draw(self):
        for i in range(self.length):
            bodyRect = pygame.Rect(self.bodyX[i],self.bodyY[i],20,20)
            pygame.draw.rect(windowSurface,GREEN,bodyRect)
    def move(self):
        
        prevX = self.bodyX[0]
        prevY = self.bodyY[0]
        self.bodyX[0] = self.headX
        self.bodyY[0] = self.headY
        for i in range(1,self.length):
            prev2X = self.bodyX[i]
            prev2Y = self.bodyY[i]
            self.bodyX[i] = prevX
            self.bodyY[i] = prevY
            prevX = prev2X
            prevY = prev2Y
        
        # Move the head according to direction.
        if self.dir == UP:
            self.headY -= 20
        if self.dir == DOWN:
            self.headY += 20
        if self.dir == LEFT:
            self.headX -= 20
        if self.dir == RIGHT:
            self.headX += 20
            
        # Check if the head exits the board, if so, put it in the opposite margin.
        if self.headX >= WIDTH - 50:
            self.headX = 50
        if self.headX <= 50:
            self.headX = WIDTH - 50
        if self.headY >= HEIGHT - 50:
            self.headY = 50
        if self.headY <= 50:
            self.headY = HEIGHT - 50
            
        # If the snake has bitten himself, restart the game.
        for i in range(self.length):
            if self.headX == self.bodyX[i] and self.headY == self.bodyY[i]:
                return False
        
        global food
        
        if self.headX == food.x and self.bodyY == food.y:
            self.length += 1
            food.x = 10+random.randint(2,27)
            food.y = 10+random.randint(2,27)
            
        return True

        
        
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
    
    #Draw the food.
    food.draw()
    
    #Draw the score.
    drawText(f"Score : {snake.length}",WIDTH//2,575,mainFont)
    
    pygame.display.update()
    

def Input(snake):
    print(1)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                print("UP")
                snake.dir = UP
            if event.key == K_DOWN or event.key == K_s:
                print("DOWN")
                snake.dir = DOWN
            if event.key == K_LEFT or event.key == K_a:
                print("LEFT")
                snake.dir = LEFT
            if event.key == K_RIGHT or event.key == K_d:
                print("RIGHT")
                snake.dir = RIGHT
            if event.key == K_ESCAPE:
                print("terminate")
                terminate()
        if event.type == QUIT:
            terminate()

food = Food(10+20*random.randint(2,27),10+20*random.randint(2,27))

def main():
    while True:
        # Initialize the snake.
        snake = Snake(WIDTH//2+10,HEIGHT//2+10)

        # Draw the "main menu" text and wait for user's input to continue or exit.
        windowSurface.fill(BLACK)
        drawText("Press enter to continue",WIDTH//2,HEIGHT//2,mainFont)
        pygame.display.update()
        waitForKey()
        
        #Game loop.
        while True:
            Draw(snake)
            Input(snake)
            if not snake.move():
                drawText("You lost",WIDTH//2,HEIGHT//2,mainFont)
                waitForKey()
                break
            mainClock.tick(10)
            
        
main()