from PythonCard import model, dialog
import random

def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations

def replace_letters(string, locations, letter):
    new_string = ""
    for i in range (0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string

class Hangman(model.Background):
    
    def on_initialize(self, event):
        self.currentworb = ""
        f = open("words.txt", "r")
        self.lines = f.readlines()
        f.close()
        self.new_game()
        
    def new_game(self):
        self.components.stYourGuesses.text = ""
        self.currentworb = random.choice(self.lines)
        self.currentworb = self.currentworb.strip()
        self.components.stDisplayWord.text = ""
        for a in range(len(self.currentworb)):
            self.components.stDisplayWord.text = self.components.stDisplayWord.text + "-"
            
        self.components.foot2.visible = False
        self.components.foot1.visible = False
        self.components.arm1.visible = False
        self.components.arm2.visible = False
        self.components.body.visible = False
        self.components.head.visible = False
        
    def on_btnGuessWord_mouseClick(self, event):
        result = dialog.textEntryDialog(self, "What is the word", "Hangman", "the word")
        self.components.stYourGuesses.text = self.components.stYourGuesses.text + " " + result.text + " "
        if result.text == self.currentworb:
            dialog.alertDialog(self, "You did it!", "Hangman")
            self.new_game()
        else:
            self.wrong_guess()
            
    def wrong_guess(self):
        dialog.alertDialog(self, "WRONG!!!", "Hangman")
        if self.components.head.visible == True:
            if self.components.body.visible == True:
                if self.components.arm1.visible == True:
                    if self.components.arm2.visible == True:
                        if self.components.foot1.visible == True:
                            if self.components.foot2.visible == True:
                                dialog.alertDialog(self, "You lost! Word was " + self.currentworb, "Hangman")
                                self.new_game()
                            else:
                                self.components.foot2.visible = True
                        else:
                            self.components.foot1.visible = True
                    else:
                        self.components.arm2.visible = True
                else:
                    self.components.arm1.visible = True
            else:
                self.components.body.visible = True
        else:
            self.components.head.visible = True
            
    def on_btnGuessLetter_mouseClick(self, event):
        result = dialog.textEntryDialog(self, "enter the letter here:", "Hangman", "")
        guess = result.text
        if len(guess) == 1:
            self.components.stYourGuesses.text = self.components.stYourGuesses.text + " " + guess + " "
            if result.text in self.currentworb:
                locations = find_letters(guess, self.currentworb)
                self.components.stDisplayWord.text = replace_letters(self.components.stDisplayWord.text, locations, guess)
                if self.components.stDisplayWord.text.find("-") == -1:
                    dialog.alertDialog(self, "You win!!!!!", "Hangman")
                    self.new_game()
            else:
                self.wrong_guess()
        else:
            dialog.alertDialog(self, "Type one letter only", "Hangman")
            
    def on_cmdNewGame_command(self, event):
        self.new_game()
app = model.Application(Hangman)
app.MainLoop()
            
        
            
        