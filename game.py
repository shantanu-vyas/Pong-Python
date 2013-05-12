import pygame, sys
from pygame.locals import *


windowHeight = 500
windowWidth = 500

windowTop = 0
windowBot = windowHeight
windowRight = windowWidth
windowLeft = 0

upPressed,downPressed = False,False 
pygame.init()                   # set up pygame stuff zzz.z.z.z.z
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("PONG")

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)


x = 0

def main():
    # init objects
    paddleLeft = Paddle(25,windowHeight/2)
    paddleRight = Paddle(475,windowHeight/2)
    ball = Ball(windowWidth/2, (windowHeight/2)+30)
    collision = False



    # while statement for ....
    while True:
        ballSpeedX=-1
        ballSpeedY=-0
        window.fill(black)
        #boundaries for the objects 
        ball.Boundaries()
        paddleLeft.Boundaries()
        paddleRight.Boundaries()
        ball.setVel(1)

        if ((ball.return_locY() > paddleLeft.return_locY() and ball.return_locY() < paddleLeft.return_locY() + 75) & (ball.return_locX() > paddleLeft.return_locX()+15)) or((ball.return_locY() > paddleRight.return_locY() and ball.return_locY() < paddleRight.return_locY() + 75) & (ball.return_locX() > paddleRight.return_locX()+15)):
            print "touching wall"
            collision == True
        else:
            print "not touching wall"



        #moves ball based on vels ballspeedx and y
        if collision == False:
            ball.moveAdd(ballSpeedX,ballSpeedY)
        else:
            ballSpeedX = *1
            ball.moveAdd(ballSpeedX,ballSpeedY)
            

        #even loop
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                # add if not_htting top boolean so the crappy animation stops same for bot...z.z.z.
                if event.key == K_UP:
                    paddleLeft.setVel(.5) 
                if event.key == K_DOWN:
                    paddleLeft.setVel(-.5)
                elif event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
            elif event.type == KEYUP:
                if event.key == K_UP or K_DOWN:
                    paddleLeft.setVel(0)

            elif event.type == pygame.QUIT:
                Pygame.display.quit()
                sys.exit()
  
        # redraw stuff
        paddleLeft.move()
        paddleLeft.draw()
        paddleRight.draw()
        ball.draw()
        pygame.display.flip()
        
    
class Paddle:
    def __init__(self,posx,posy):
        self.paddleX = posx
        self.paddleY = posy
        self.velocity = 0

    def draw(self):
        # 25,250
        pygame.draw.line(window,white,(self.paddleX,self.paddleY),(self.paddleX,self.paddleY+75),10)

    def return_locX(self):
        return self.paddleX

    def return_locY(self):
        return self.paddleY

    def setLocX(self,val):
        self.paddleX = val

    def setLocY(self,val):
        self.paddleY = val
    def setVel(self,number):
        self.velocity = number
    def move(self):
        self.paddleY = self.paddleY - self.velocity



    def Boundaries(self):
        if self.paddleX <= windowLeft+10:
            self.paddleX = windowLeft+10
        if self.paddleX >= windowRight-10:
            self.paddleX = windowRight-10
        if self.paddleY <= windowTop+10:
            self.paddleY = windowTop+10
        if self.paddleY >= windowBot-85:
            self.paddleY = windowBot-85
            
    # if methodBallX == self.paddleX & methodBallY == self.paddleY:
    #         #set ball values to padle values
    #         methodBallX

class Ball:
    def __init__(self,posx,posy):
        self.ballX = posx
        self.ballY = posy

    def draw(self):
        pygame.draw.circle(window,blue,(self.ballX,self.ballY),10,0)

    def return_locX(self):
        return self.ballX

    def return_locY(self):
        return self.ballY

    def setLocX(self,val):
        self.ballX = val

    def setLocY(self,val):
        self.ballY = val
    def setVel(self,num):
        self.vel = num
    def returnVel(self):
        return self.vel
    def moveAdd(self,newx,newy):
        self.setLocX(self.return_locX()+newx)
        self.setLocY(self.return_locY()+newy)
    
    
    def Boundaries(self):
        if self.ballX <= windowLeft+10:
            self.ballX = windowLeft+10
        if self.ballX >= windowRight-10:
            self.ballX = windowRight-10
        if self.ballY <= windowTop+10:
            self.ballY = windowTop+10
        if self.ballY >= windowBot-10:
            self.ballY = windowBot-10

    def colisionBoundaries(self):
        if self.ballX <= windowLeft+25:
            self.ballX = windowLeft+25
        if self.ballX >= windowRight-25:
            self.ballX = windowRight-25
        if self.ballY <= windowTop+10:
            self.ballY = windowTop+10
        if self.ballY >= windowBot-10:
            self.ballY = windowBot-10
            
        print "asdfasdf"

    

# #return_ballX = 'return_locX'
# methodBallX = getattr(Ball, 'return_locX')
# methodBallY = getattr(Ball, 'return_locY')
# methodSetBallX = getattr(ball, 'set_locX()')
# methodSetBallY = getattr(ball, 'set_locY()

main()




