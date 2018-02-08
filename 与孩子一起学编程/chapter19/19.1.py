import random, pygame, sys

def printWordsInScreen(words,y_pos,delayTime):
    i = 0
    for word in words:
        score_text = font.render(word, 1, (0, 0, 0))
        screen.blit(score_text, [10, y_pos + 30 * i])
        pygame.display.flip()
        pygame.time.delay(delayTime)
        i += 2
        
def clearScreen():
    screen.fill([255, 255, 255])
    pygame.display.flip()
    
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.display.flip()
pygame.time.delay(1000)

font = pygame.font.Font(None, 50)


guess = 0
tries = 0

windowsShutDown = False
playAgain = True

ahoy = pygame.mixer.Sound("Ahoy.wav")
tooLow = pygame.mixer.Sound("TooLow.wav")
tooHigh = pygame.mixer.Sound("TooHigh.wav")
askGuess = pygame.mixer.Sound("WhatsYerGuess.wav")
gotIt = pygame.mixer.Sound("AvastGotIt.wav")
noMore = pygame.mixer.Sound("NoMore.wav")

while playAgain:
    secret = random.randint(1, 100)
    ahoy.play()
    ahoyWords = ["AHOY! I'm the Dread Pirate Roberts.","And I have a secret!","It is a number from 1 to 99.","I'll give you 6 tries."]
    printWordsInScreen(ahoyWords,50,2000)
    clearScreen()

    while guess != secret and tries < 6:
        askGuess.play()
        askGuessWords = ["What's yer guess?","Input yer guess by Keyboard","Finish confirm by pressing enter key."]
        printWordsInScreen(askGuessWords,20,100)
        guessInputComplete = False
        inputStr = ""
        while not guessInputComplete:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if inputStr == "":
                            guessInputComplete = False
                        else:
                            guessInputComplete = True   
                    elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                        inputStr = inputStr + chr(event.key) #chr() converts ascii to str
                pygame.time.delay(100)
        printWordsInScreen(["Your guess is " + inputStr + "."],200,100)
        guess = int(inputStr)
        if guess < secret:
            tooLow.play()
            printWordsInScreen(["Too low, ye scurvy dog!"],260,100)
            pygame.time.delay(3000)
        elif guess > secret:
            tooHigh.play()
            printWordsInScreen(["Too high, landlubber!"],260,100)
            pygame.time.delay(3000)
        else:
            pygame.time.delay(1500)
        tries = tries + 1
        clearScreen()
    if guess == secret:
        gotIt.play()
        printWordsInScreen(["Avast! Ye got it! Found my secret","The Secret is " + str(secret) + ". ye did!"],140,100)
    else:
        noMore.play()
        printWordsInScreen(["No more guesses!","Better luck next time, matey!","The Secret is " + str(secret) + "."],140,100)
    pygame.time.delay(4000)
    clearScreen()
    printWordsInScreen(["Would you play one more time?","Input y means yes","Input n means no"],140,100)
    answerComplete = False
    while not answerComplete:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    answerComplete = True
                    playAgain = True
                    tries = 0
                elif event.key == pygame.K_n:
                    answerComplete = True
                    playAgain = False
                else:
                    answerComplete = False
            pygame.time.delay(100)
    clearScreen()
sys.exit()
        