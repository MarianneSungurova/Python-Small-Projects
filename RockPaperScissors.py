import random as rdm 
import os
import sys

def pc_turn():    
    Possible_values=["Rock", "Scissors","Paper"]
    return rdm.choice(Possible_values)


def get_user_action(): 
    user_turn=input("Your turn: ")



while True:
    computer=pc_turn()
    user_turn=get_user_action()
    if user_turn==computer:
        print("Draw")
    elif user_turn=="Rock":
        if computer=="Scissors": print("You've won")
        else: print("You've lost")
    elif user_turn=="Scissors": 
        if computer=="Paper": print("You've won")
        else: print("You've lost")
    else: 
        if computer=="Rock": print("You've won")
        else: print("You've lost")

    restart=input("Press y to restart the game\n ")
    if restart!="y": break

