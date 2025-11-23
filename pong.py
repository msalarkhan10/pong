import pygame
import random


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))
        self.ball = Ball()
        self.paddle_1 = Padle(50)
        self.paddle_2 = Padle(800-80)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        

    def run(self):
        while True:
            pygame.event.get()

            keys =pygame.key.get_pressed()
            if keys [pygame.K_UP]:
                self.paddle_1.move("UP")
            if keys [pygame.K_DOWN]:
                self.paddle_1.move("DOWN")

            if keys [pygame.K_w]:
                self.paddle_2.move("UP")
            if keys [pygame.K_s]:
                self.paddle_2.move("DOWN")
            

            if self.ball.wallCollision():
                self.ball.changey()

            if self.ball.paddleCollision(self.paddle_1,"LEFT"):
                self.ball.changex(1)

            if self.ball.paddleCollision(self.paddle_2,"RIGHT"):
                self.ball.changex(-1)

            if self.ball.x < 0:
                self.ball.reset(1)

            if self.ball.x > 800:
                self.ball.reset(-1)

            self.paddle_1.show(self.display)
            self.paddle_2.show(self.display)
            self.ball.show(self.display)
            pygame.display.update()
            self.ball.move()
            self.display.fill((0,0,0))
            self.clock.tick(60)


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
        pygame.draw.rect(display , self.colour, (self.x , self.y, self.width, self.height))

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

    def move(self):
        self.x+= self.speed*self.x_direction
        self.y+= self.speed*self.y_direction
        

    def paddleCollision(self,paddle,paddle_direction):
        match(paddle_direction):
            case "LEFT":
                return self.x < paddle.x + paddle.width and paddle.y <self.y < paddle.y + paddle.height
            case "RIGHT":
                return self.x > paddle.x and paddle.y <self.y < paddle.y + paddle.height
            

    def wallCollision(self):
        return self.y  < 0 or self.y>600 - self.size
    
    def show(self,display):
        pygame.draw.circle(display , self.colour, (self.x, self.y), self.size)

    def reset(self,x_direction):
        self.x=800/2 - self.size/2
        self.y=600/2 - self.size/2
        self.x_direction = x_direction
        self.y_direction= random.choice([1,-1])





  
def main():
    pygame.init()
    
    GAME=Game()
    GAME.run()

main()