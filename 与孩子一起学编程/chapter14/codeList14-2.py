'''
It seems that the property of the object can be given without any definition.
Just like the variable, you don't need to define the variable.

'''

class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"
myBall.owner = "yveon_ou"  #add it myself

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "My ball's owner is", myBall.owner #add it myself
print "Now I'm going to bounce the ball"
print
myBall.bounce()
print "Now the ball's direction is", myBall.direction
