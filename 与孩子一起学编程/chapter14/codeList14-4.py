class Ball:
    def __init__(sel, color, size, direction):
        sel.color = color
        sel.size = size
        sel.direction = direction

    def __str__(sel):
        msg = "Hi, I'm a " + sel.size + " " + sel.color + " ball!"
        return msg

myBall = Ball("red", "small", "down")
print myBall
