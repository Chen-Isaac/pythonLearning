import sys, pygame, random

#----ball subclass definition --------------------
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        
    def move(self):
        self.rect = self.rect.move(self.speed) #only get the rect
        if self.rect.left < 0 or self.rect.right > width: #width is a global variable
            self.speed[0] = -self.speed[0]
            
        if self.rect.top < 0 or self.rect.bottom > height: #height is a global variable
            self.speed[1] = -self.speed[1]
            
#--------------Main Program----------------------------------------
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "beach_ball.png"
balls = []
for row in range (0, 3):
    for column in range (0, 3):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [random.choice([-2, 2]), random.choice([-2, 2])]
        ball = MyBallClass(img_file, location, speed)
        balls.append(ball)
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.time.delay(20)
    screen.fill([255, 255, 255])   #erase the old frame
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
        #pygame.time.delay(1000)
    pygame.display.flip()
