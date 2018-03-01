from PythonCard import model
import random, time

secret = random.randint(1, 100)
guess = 0
tries = 0

class MainWindow(model.Background):
    
    def on_cofBtn_mouseClick(self, event):
        global tries, guess
        if guess != secret and tries < 6:
            self.components.guessNum.enabled = 1
            guess = self.components.guessNum.value
            if guess < secret:
                self.components.result.text = "Too low, ye scurvy dog!"
            elif guess > secret:
                self.components.result.text = "Too high, landlubber!"
            tries += 1
        elif tries >= 6:
            self.components.result.text = "No more guesses! Better luck next time, matey!"
            time.sleep(0.5)
            self.components.result.text = "The secret number was " + str(secret)
            self.components.guessNum.enabled = 0
        else:
            self.components.result.text = "Avast! Ye got it! Found my secret, ye did!"
            self.components.guessNum.enabled = 0
            
    def on_replay_mouseClick(self, event):
        global tries, guess, secret
        self.components.guessNum.value = 0
        self.components.guessNum.enabled = 1
        tries = 0
        guess = 0
        secret = random.randint(1, 100)
        self.components.result.text = ""
       
        
app = model.Application(MainWindow)
app.MainLoop()

    