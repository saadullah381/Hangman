# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:25:34 2020

@author: hp
"""

import random #For the random word choices
import time #For the pause time 
print("Welcome to HANGMAN")
time.sleep(0.3) #Give player some time before playing
print("You only have 5 guesses to save the man!") #Tell them the amount of guesses they have
def hangMan(): #When players lose the hangman will show to indicate they lost the game
  return("""
           |---|
           O   |
          /|\  |
          / \  |
               |
       =========""")
  print(hangMan)
def theMan(): #theMan is the symbol to show that you won and saved the man
  return("""  
            O 
           /|\\
           / \\
         =========""")
  print(theMan())
def getGuess(): #Get players guess
  dashes = "*" * len(secretWord)
  guessesLeft = 5
  while guessesLeft > -1 and not dashes == secretWord:
    print(dashes)
    print (str(guessesLeft))
    print("This is the second letter",second)
    print("This is the fifth letter",fifth)
    guess = input("Guess:")
    if len(guess) != 1: #Can only guess 1 letter at a time
      print ("Your guess must have exactly one character!")
    elif guess in secretWord:
      print ("That letter is in the secret word!")
      dashes = updateDashes(secretWord, dashes, guess) #To udate the dashes everytime you get something right.
    else:
      print ("That letter is not in the secret word!")
      guessesLeft -= 1 #To subtract a guess everytime you get a wrong letter
  if guessesLeft < 0:
    print ("You lose. The word was: " + str(secretWord))
    print(hangMan())
  else:
    print ("Congrats! You win. The word was: " + str(secretWord))
    print(theMan())
    print("You saved me! Thank you! :D")

def updateDashes(secret, currentDash, recGuess):
  result = ""
  
  for i in range(len(secret)): #To get the dashes to update if correct or not
    if secret[i] == recGuess:
      result = result + recGuess  
      
    else:
      result = result + currentDash[i]
      
  return result
with open("4words.csv") as file:
    data= file.read()
word1= data.split()
secretWord= random.choice(word1)
first=secretWord[0]
second=secretWord[1]
third=secretWord[2]
fourth=secretWord[3]
fifth=secretWord[4]

#words = ["pie","hello","yanny","laurel","bomb","math","program","web design","english","dogs","food","game","hangman","fountain valley high school"]

#secretWord = random.choice(words) #Random choice of words 
getGuess() #To get the guess of the player