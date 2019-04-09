import requests
import random
import time
import os

def game():
  levels = 0

  guess = 6

  score = -1

  game_intro()

  game_on = True

  while game_on:
      score = score + 1
      levels = levels + 1
      guess = 6
      word = get_wordlist(levels)
      level_intro(levels, guess, score)
      word, guess, score, levels, game_on = level(word, guess, score, levels, game_on)
      if levels == 10:
        break

  time.sleep(3)      
  print("\nGame Over.  Your final score is " + str(score))


def get_wordlist(levels):

  url = 'http://app.linkedin-reach.io/words?difficulty=' + str(levels)

  response = requests.get(url)

  data = response.text

  word_list = data.split('\n')

  word = random.choice(word_list)
  
  return (word)

def game_intro():
  os.system("clear")
  print('Welcome to Word Guessing Game\n')
  time.sleep(3)
  print('I am a secret-keeper and you will be guessing what word I am thinking of. \n')
  time.sleep(3)
  print('For each level, you will have six guesses to enter a letter you think is in the word.  There are 10 levels with difficulty increasing with each level.')
  time.sleep(5)
  os.system("clear")

def screen_layout(levels, guess, score):
  print("Level: " + str(levels))
  print("Score: " + str(score))
  print("Guess Left: " + str(guess))

def level_intro(levels, guess, score):
  screen_layout(levels, guess, score)
  print("\n\nLevel " + str(levels) )
  print("\nPlease guess what word I am thinking.  You will have six guesses.")
  time.sleep(3)
  os.system("clear")

def level(word, guess, score, levels, game_on):
  blank =  ['_'] * len(word)
  incorrect_letters = []
  win = True

  while win:
      screen_layout(levels, guess, score)
      if '_' in blank:
        print("\nWord:    " + ' '.join(blank))
        blank, word, guess, incorrect_letters, win = guessing(blank, word, guess, incorrect_letters, win)
        os.system("clear")
  
  if guess == 0:  
    art(guess)    
    print("No more guess left")
    print("\nThe word was: " + word)
    game_on = False
  else:
    print("You guessed the word!\n")
    time.sleep(3)
    os.system("clear")

  return (word, guess, score, levels, game_on)

def guessing(blank, word, guess, incorrect_letters, win):
  
  original = blank[:]

  art(guess)

  print("\nIncorrect letters: " + " ".join(incorrect_letters))

  while True:
    letter = input("\nPlease guess a letter: ").lower()
    if letter.isalpha() and len(letter) == 1:
      break
    print("Please enter only one letter between a-z only.")  

  blank[:] = [letter if letter == word[i] else x for i, x in enumerate(blank)]
  
  if blank == original:
    incorrect_letters.append(letter)
    guess = guess - 1

  if guess == 0 or '_'  not in blank:
    win = False

  return (blank, word, guess, incorrect_letters, win)

def art(guess):
  #5: head, 4:body, 3:left arm, 2: right arm, 1: left leg, 0: right leg)

  body_parts = {

  5: chr(32) + chr(124) + chr(32) * 3 + chr(210),

  4: chr(32) + chr(124) + chr(32) * 3 + chr(124) + "\n" + chr(32) + chr(124) + chr(32) * 3 + chr(124),

  3: chr(32) + chr(124) + chr(32) * 2 + chr(47) + chr(124) + "\n" + chr(32) + chr(124) + chr(32) * 3 + chr(124),

  2: chr(32) + chr(124) + chr(32) * 2 + chr(47) + chr(124) + chr(92)  + "\n" + chr(32) + chr(124) + chr(32) * 3 + chr(124),

  1: chr(32) + chr(124) + chr(32) * 2 + chr(47),

  0: chr(32) + chr(124) + chr(32) * 2 + chr(47) + chr(32)+ chr(92)

  }

    #1
  print(chr(32) * 2 + (chr(95) * 3))
  #2
  print(chr(32) + chr(124) + chr(32) * 3 + chr(124))
  #3 head 
  print(body_parts[5] if guess <= 5 else chr(32) + chr(124)) 
  #body 
  #print( body_parts[4] if guess == 4 else chr(32) + chr(124))

  if guess > 4: 
    print(chr(32) + chr(124))
  elif guess == 4:
    print(body_parts[4])
    
  if guess == 3:  
    print(body_parts[3])

  if guess <= 2:
    print(body_parts[2])

  print(body_parts[1] if guess == 1 else chr(32) + chr(124))

  if guess == 0:
    print(body_parts[0])
  
  #7stand
  print((chr(45) * 3))


  
 

game()

