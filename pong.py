import pygame
import random

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))


WHITE = (255,255,255)
class Padle:
    def __init__(self,x):
        self.width= 10
        self.height= 80
        self.x= x
        self.y= 600/2 -  self.height/2
        self.speed=5
        self.colour= WHITE


    def move(self, direction):
        match direction:
            case "UP":
                if (self.y> 0):
                    self.y -= self.speed
            case "DOWN":
                if (self.y<600 -self.height):
                    self.y += self.speed
            case _:
                pass

    def show(self,display):
        pygame.draw.rect(display , self.colour, (self.x , self.y, self.height, self.width))

class Ball:
    def __init__(self):
        self.size = 5
        self.x = 800/2 - self.size /2
        self.y = 600/2 - self.size/2
        self.speed = 4
        self.colour = WHITE
        self.x_direction= random.choice([ 1 , -1])
        self.y_direction= random.choice([ 1 , -1])

    def changex(self, direction):
        self.x_direction= direction

    def changey(self):
        self.y_direction = - self.y_direction







  
def main():
    pygame.init()

main()