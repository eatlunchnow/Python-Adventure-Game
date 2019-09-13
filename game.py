import time 
import math
import pprint
import itertools
from itertools import permutations

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["yes"]
no = ["no"]
directions = ["left", "right", "forward", "backward"]
score = 0

required = ("\nUse only A, B, C, yes, or no, or specific numbers to answer\n") 
required_dir = ("\nUse only right, left, backward, or forward to answer\n") 
required_weapons = ("\nUse only Dagger, Flail, or Lance to answer") 

def intro():
  print ("Are you ready to play? (yes/no)")
  time.sleep(1)
  choice = input(">>> ") 
  if choice in yes:
    option_nameChange()
  elif choice in no:
    print ("Okay then, goodbye!")
  else:
    print (required)
    intro()

def option_nameChange(): 
  print ("\nYou are a math wizard at a school for gifted math wizards. Everyone has a special code they must go by instead of their real names. Let's use a cipher to determine your name code.")
  start = 2
  end = 103

  primenums = []

  for primeNum in range(2, 103):
     isPrimeNum = True
     for num in range(2, primeNum):
            if (primeNum % num) == 0:
                isPrimeNum = False

     if isPrimeNum:
         primenums.append(primeNum)

  alphabet =[]
  for letter in range(97, 123):
    alphabet.append(chr(letter))

  cipher = dict(zip(primenums, alphabet))

  numparray =[]
  initials = input("Enter your initials: ")
  list(initials)
  def SASPrimeCipher():
    for letter in initials:
      numparray.append()
      result = 1
      for x in numparray:
        result = result * x
        return result 
  print("\nYour magic math name is: " + str(letter))
  print("Hello magic wizard " + str(letter)+ "! Let's start!")
  print("\n")
  
  print(str(letter) + ", you are at school in your least favorite class, gym. You have to play baseball and you hate baseball. You have to be pitcher and the biggest boy in school comes up to the plate to bat. You pitch, hear the crack of the ball hitting the bat. Next thing you see is the baseball flying toward your face. Everything turns black. You wake up in a white room with a wooden door. Do you want to go through the door? (yes/no")
  time.sleep(1)
  choice = input(">>> ") 
  if choice in yes:
    option_unlockDoor()
  elif choice in no:
    print ("Looks like you are stuck in this room. Goodbye!")
  else:
    print (required)
    #intro()

def option_unlockDoor():
  print ("\nAbove the door it says, 'To make it through this door finary, convert the number 12 to binary'. Shall we convert it? (yes/no")
  choice = input(">>> ") 
  if choice in yes:
    door_open()
  elif choice in no:
    print ("\nI guess you really want to be stuck in this room!")
  else:
    print (required)
    option_unlockDoor()

def door_open():
  bi_convert = input("Enter the number 12: ")
  bi_convert_i = int(bi_convert)
  def dec2bin(bi_convert_i):
    if bi_convert_i > 1:
        dec2bin(bi_convert_i // 2)       
    print(bi_convert_i % 2, end='')
  convert_code = dec2bin(bi_convert_i)
  print(convert_code)


  door_code = input("Enter binary number to open door: ")
  door_code_i = int(door_code)
  def openDoor():
    if door_code_i == 1100:
      global score
      score += 1
      print("\nYou opened the door! You walk through the door and find a whimsical world of numbers, math, creatures, and magical lands.")
      time.sleep(1)
      option_bridge()
    else:
     print("Door is still closed. Try again!")
     door_open()
     print(required)
  openDoor()

def option_bridge():
  def star_row(n): 
    if (n < 1): 
        return
    print("*", end = " ") 
    star_row(n - 1) 
  
  def print_star(n): 
    if (n < 1): 
        return
    star_row(n)  
    print("") 
    print_star(n - 1) 
    
  n = 5
#print_star(n)

  print("\nYou come to a wide river with sparkly pink water. There is a bridge but part of it is gone. A sign next to the river has this pattern:") 
  print_star(n)
  print("If you correctly say the number of rows in the pattern the bridge will magically repair itself.")
  choice = input("You say: ")
  time.sleep(1)
  if choice == "5":
    global score
    score += 3
    print("\nYou got it! The bridge extends to the other side of the shore. Walk across.")
    option_combo()
  else:
    print("\nNo, wrong answer. A hole opens up and swallows you. You are deceased.")

def option_combo():
  values = ["The Magician", "The Hermit", "The Blacksmith", "The Loser", "The Winner", "The Scoundrel", "The Servent"]
  result = itertools.combinations(values, 3)
  lstres = list(result)
  result_s =  str(len(lstres))
  #result = itertools.combinations(values, 3)
  
  print("\nYou get to the shore to see an elf seated at a table with 7 cards lying face down. As you approach, the elf slowly turns each one other revealing The Magician, The Hermit, The Blackmisth, The Loser, The Winner, The Scoundrel, and The Servent. The elf asks how you many combinations of 3 cards are there?  ")
  choice = input(str("Your answer: "))
  time.sleep(1)
  if choice == result_s:
    global score
    score += 5
    print("\nYes! The elf gifts you all the cards except The Loser card. You may continue on.")
    option_factorial()
  else:
    print("\nNot correct! The elf throws The Loser card at you. Game over!") 

def option_factorial():
  def factorial(n):
    if n == 1:
      return 1
    else:
      x = factorial(n - 1)
      print( n, "*", x )
      return n * x

  print("\nYou pass by a nymph that is lost and asks for your help. She says she needs to know what the factorial of 6 is to find her map to get her back home. She asks you to help her. Figure out what 6! is.") 
  user_input = input("Enter the number 6: ")
  print("The list of factorials are listed for you. Multiply the correct one to get the nymph back home.")
  n = int(user_input)
  answer = factorial(n)
  answer_i = str(answer)

  choice = input("Your answer: ")
  time.sleep(1)
  if choice == answer_i:
    global score
    score += 2
    print("\nCorrect! The nymph finds her map. She thanks you and begins her journey home.")
    time.sleep(1)
    option_knightFight()
  else:
      print("\nWrong answer. The nymph claws at you until you die. You died!") 

def option_knightFight():
  print ("\nAfter the nymph leaves you continue on but reach a knight. He says you can not pass without a fight. Luckily, there is a weapons tree right next to you. The count of each weapon in the tree is below. Which weapon(s) do you want? (please enter Dagger, Flail, or Lance)")

  class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        return '{0}, count: {1}'.format(self.value, self.count)

  def insert(root, value):
      if not root:
        return Node(value)
      elif root.value == value:
        root.count += 1
      elif value < root.value:
        root.left = insert(root.left, value)
      else:
        root.right = insert(root.right, value)

      return root

  def create(order):
      root = None
      for word in order:
        root = insert(root, word)

      return root

  def search(root, word, depth=1):
      if not root:
        return 0, 0
      elif root.value == word:
        return depth, root.count
      elif word < root.value:
        return search(root.left, word, depth + 1)
      else:
        return search(root.right, word, depth + 1)

  def print_tree(root):
      if root:
        print_tree(root.left)
        print(root)
        print_tree(root.right)

  src = ["Dagger", "Flail", "Flail", "Lance", "Lance", "Dagger", "Lance"]
  tree = create(src)
  print_tree(tree)

  choice = input(">>> ")
  time.sleep(1)
  if choice == "Dagger":
    global score
    score += 6
    print("\nYou have two Daggers! You put up a spirited fight and you defeat the knight!")
    time.sleep(1)
    option_directions()
  elif choice == "Flail":
    score += 6
    print("\nYou have two Flails! You put up a spirited fight and you defeat the knight!")
    time.sleep(1)
    option_directions()
  elif choice == "Lance":
    score += 6
    print("\nYou have three Lances! You put up a spirited fight and you defeat the knight!")
    time.sleep(1)
    option_directions()
  else:
    print(required_weapons)
    option_knightFight()

def option_directions():
  print("\nGreat job on defeating the knight!")
  time.sleep(1)
  print("\nThere is a whole new world in front of you!")
  print("To your right is a number gobbler.")
  print("To your left you see a an orge having a picnic.")
  print("If you go backwards there is a coven of witches.")
  print("If you go forward there is a numbers hurricane.")
  print("Which direction do you go? (right, left, backward, forward)")
  choice = input(">>> ")
  if choice == "right":
    option_right()
  elif choice == "left":
    option_left()
  elif choice == "backward":
    option_backward()
  elif choice == "forward":
    option_forward() 
  else:
    print (required_dir)
    option_directions()
    
def option_right():
  print ("\nYou have chosen to battle the number gobbler monster! There are two tables of weapons available. Some similar, some different. We must create an intersection of all the weapsons to defeat the number gobbler. The red table has a knife, machete, sword, and crossbow. The blue table has a battle ax, knife, spear, and machete. We need duplicate weapons to defeat the monster.")

  weapon_set1 = {"knife", "machete", "sword", "crossbow"}
  weapon_set2 = {"battle ax", "knife", "spear", "machete"}
  intersection = weapon_set1 & weapon_set2
  #print(intersection)
  print("\nWhat two weapons do we use? ")
  print("A. knife and machete")
  print("B. battle ax and spear")

  choice = input(">>> ")
  if choice in answer_A:
    battle_ax = 1
  else:
    battle_ax = 0
  time.sleep(1)
  if battle_ax > 0:
    global score
    score += 3
    print ("\nYou wield the battle ax and machete with precision. You killed the number gobbler! You win! Your score is: " + str(score))
  else: 
     print ("\nYou picked the wrong weapons. You died!")

def option_left():
  print("\nYou join the ogre on their picnic. He has three fruits: an apple, a banana, an orange. He wants to play a game to find out how many permutations of the fruit you can create. ")
  fruits = ["apple", "banana", "orange"]
  fruit_trios = permutations(fruits, 3)

  count = 0
  for i in list(fruit_trios):
    #print(i)
    count = count + 1 
  
  count_fruit = len(fruits)
  perm_ans= str(math.factorial(count_fruit))
  choice = input("Your answer: ") 
  if choice == perm_ans:
    global score
    score += 4
    print("\nCorrect! You and the orge share the fruit! Your score is: " + str(score))
  else:
      print("\nWrong answer. The orge takes all the fruit then hits you on the top of your head with his fist. You are dead.")
  #option_left()

def option_backward():
  print("\nThere are 5 witches around a cauldron. They are bickering like no tomorrow. With conflicts like that they must be related. What is the percentage probability that 3 of them are sisters? (do not include the percentage symbol in your answer)")
  witches = 5
  sisters = 3

  sis_prob_div = sisters/witches
  sis_prob_percent = sis_prob_div * 100
  sis_ans = (str(round(sis_prob_percent)))
 
  choice = input("Your answer: ")
  time.sleep(1) 
  if choice == sis_ans:
    global score
    score += 4
    print("\nThat's right! The witches cast a spell on you for good fortune. Your score is: " + str(score))
  else:
    print("\nWrong answer. The witches throw you in the cauldron.")


def option_forward():
  print ("\nTry your best not to get blown away as you head toward the number hurricane. You see the numbers 6, 19, 35, 22, 4, 81, 57 being swirled and tossed about. A jester skips by you and says first: 'In order to not blow away the fort, use bubble sort' then says: 'To make sure you don't fall short, use insertion sort'. Which sort do you use? ")
  print("A. 'In order to not blow away the fort, use bubble sort'")
  print("B. 'To make sure you don't fall short, use insertion sort'")
  choice = input(">>> ")
  if choice in answer_A:
    global score
    score += 2
    bubble_sort_spell()
  elif choice in answer_B:
    score += 2
    insertion_sort_spell()
  else:
     print ("\nYou got swept away in the hurricane!")

def bubble_sort_spell():
  def bubble_sort(bubList):
    n = len(bubList)
    for i in range(n):
      for j in range(0, n - i - 1):
        if bubList[j] > bubList[j + 1]:
          bubList[j], bubList[j + 1] = bubList[j + 1], bubList[j]
    return bubList   

  bubList = [6, 19, 35, 22, 4, 81, 57]
  print("Numbers in order: " + str(bubble_sort(bubList)))
  print("The numbers are in order from the bubble sort number order spell. The hurricane is gone! Your score is: " + str(score))

def insertion_sort_spell():
  def insertion_sort(insertList):
    for i in range(1, len(insertList)):
      temp = insertList[i]
      j = i - 1
    while (j >= 0 and temp < insertList[j]):
      insertList[j + 1] = insertList[j]
      j = j - 1
      insertList[j + 1] = temp
 
  insertList = [6, 19, 35, 22, 4, 81, 57]
  print(insertion_sort(insertList))
  print("Numbers in order: " + str(insertList))
  time.sleep(1) 
  print("The numbers are in order from the insertion sort number order spell. The hurricane is gone! Your score is: " +  str(score))