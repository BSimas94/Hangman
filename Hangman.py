#---------------------------------------------
#Hangman Game
#Author: Blake Simas
#---------------------------------------------

import random

def randword():
    wordBank = ["computer","president","trojan","program","coffee", "library","football","popcorn","science","engineer","rhythm"]
    word = random.choice(wordBank)
    return word

#Generate random word from list above at the start of program
word = str(randword())
playing = True
correctLetters = ""
missedLetters = ""
lives = 8

#Intro
print("\n--------------------Hangman--------------------")
print("--------Developed by Blake Simas (2016)--------\n")
print("Enter a character to guess:")
blanks = "*"*len(word)
print(blanks)
print("\n**Type 'quit' to end the game.")

#Loop for user guesses
while playing == True and lives > 0:
    for char in word:
        guess = str(raw_input("\nGuess a letter or the word: "))
        if guess == "quit":
            quit()
        elif len(guess) != 1:
            print("\nPlease enter ONLY one letter.")
            break
        elif guess.islower() == False:
            print("\nEnter only lower case letters.")
            break
        if guess in word:
            correctLetters += guess
            print("\nYou guessed correctly!\n")
            for i in range(len(word)):
                if word[i] in correctLetters:
                    blanks = blanks[:i] + word[i] + blanks[i+1:]
            for letter in blanks:
                print letter,
            print("")
            if blanks == word:
                print ("\nYou win! You guessed the word {} with {} lives left.\n".format(word, lives))
                playing = False
                quit()
        else:
            print("\nThis word does not contain that letter.\n")
            lives -= 1
            print ("You have {} lives left.".format(lives))
        if lives == 0:
            print("\nGame Over!")
            playing = False
            quit()
