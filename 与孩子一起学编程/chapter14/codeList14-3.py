'''
It seems that the property of the object can be given after init.
'''

class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball("red", "small", "down")
myBall.owner = "yveon_ou"  #add it myself
print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is ", myBall.direction
print "My ball's owner is", myBall.owner #add it myself
print "Now I'm going to bounce the ball"
print
#myBall.bounce()
Ball.bounce(myBall) #it = myBall.bounce()
print "Now the ball's direction is", myBall.direction
print myBall
