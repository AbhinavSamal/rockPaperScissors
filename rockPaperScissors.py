from ast import Import
from random import random


import random
import time 

options = ['Rock', 'Paper' , 'Scissors']

while True:
    computer = random.choice(options)
    player = input("Choose any one - (Rock/Paper/Scissors)")

    if player == computer:
        print("It's a tie")

    if player == "Rock":
        time.sleep(3)
        if computer == "Paper":
            print("You loose!! paper covers the rock.")
        elif computer == "Scissors":
            print("You won!! rock broke the scissors")
    elif player == "Paper":
        time.sleep(3)
        if computer == "Rock":
            print("You won!! paper covers the rock.")
        elif computer == "Scissors":
            print("You loose!! scissors cuts the paper")
    else :
        time.sleep(3)
        if computer == "Paper":
            print("You won!! scissors cuts the paper")
        elif computer == "Rock":
            print("You loose!! rock broke the scissors")
