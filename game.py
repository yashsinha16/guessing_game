"""GuessingGame"""
import os
import getpass
import pandas as pd


def login():
    """LoggingIntoGame"""
    user_data = pd.read_csv("username.csv")
    user_data = user_data.set_index("username")
    flag_1 = 0
    while flag_1 == 0:
        username = input("please enter your username: ")
        if username in user_data.index:
            password = input("please enter your password: ")
            if password == user_data.at[username, "password"]:
                flag_1 = 1
                os.system("cls" if os.name == "nt" else "clear")
                print("you have logged in succesfully")
                user_data.at[username, "attempts"] += 1
                user_data.to_csv("username.csv")
            else:
                print("invalid password")
        else:
            print("invalid login credentials")


login()


TOTALGUESSES = 1
MAX_NUMBER = [20, 40, 60]
USER1 = input("Player 1 please enter your name:  ")
USER2 = input("Player 2 please enter your name:  ")
LEVELS = ["easy", "medium", "hard"]
DIFFICULTY = input("select difficulty level:EASY,MEDIUM or HARD: ")
B = int(input(USER2 + " how many guesses will you need: "))
COUNT = 0
if DIFFICULTY == LEVELS[0]:
    while COUNT == 0:
        GUESSED = getpass.getpass(USER1 + " enter between 1 and 20:  ")
        if int(GUESSED) > MAX_NUMBER[0]:
            print("Number is out of bounds")
        else:
            COUNT = 1
        GUESS_USER1 = GUESSED
    while TOTALGUESSES <= B:
        TOTALGUESSES = TOTALGUESSES+1
        C = int(input(USER2 + " take a guess: "))
        if int(GUESS_USER1) == C:
            print(USER2 + " you have guessed it")
            break
        elif C > int(GUESS_USER1):
            print("It's too high")
        elif C < int(GUESS_USER1):
            print("Too low!!")
        elif int(GUESS_USER1) > MAX_NUMBER[0]:
            print("guess is out of bounds")
    if TOTALGUESSES > B + 1:
        print("out of guesses")
    print("the right number is %d" % int(GUESS_USER1))
if DIFFICULTY == LEVELS[1]:
    while COUNT == 0:
        GUESSED = getpass.getpass(USER1 + " enter between 1 and 40:  ")
        if int(GUESSED) > MAX_NUMBER[1]:
            print("Number is out of bounds")
        else:
            COUNT = 1
        GUESS_USER1 = GUESSED
    while TOTALGUESSES <= B:
        TOTALGUESSES = TOTALGUESSES+1
        C = int(input(USER2 + " take a guess: "))
        if int(GUESS_USER1) == C:
            print(USER2 + " you have guessed it")
            break
        elif C > int(GUESS_USER1):
            print("It's too high")
        elif C < int(GUESS_USER1):
            print("Too low!!")
        elif int(GUESS_USER1) > MAX_NUMBER[1]:
            print("guess is out of bounds")
    if TOTALGUESSES > B:
        print("out of guesses")
    print("the right number is %d" % int(GUESS_USER1))
if DIFFICULTY == LEVELS[2]:
    while COUNT == 0:
        GUESSED = getpass.getpass(USER1 + " enter between 1 and 60:  ")
        if int(GUESSED) > MAX_NUMBER[2]:
            print("Number is out of bounds")
        else:
            COUNT = 1
        GUESS_USER1 = GUESSED
    while TOTALGUESSES <= B:
        TOTALGUESSES = TOTALGUESSES+1
        C = int(input(USER2 + " take a guess: "))
        if int(GUESS_USER1) == C:
            print(USER2 + " you have guessed it")
            break
        elif C > int(GUESS_USER1):
            print("It's too high")
        elif C < int(GUESS_USER1):
            print("Too low!!")
        elif int(GUESS_USER1) > MAX_NUMBER[2]:
            print("guess is out of bounds")
    if TOTALGUESSES > B:
        print("out of guesses")
    print("the right number is %d" % int(GUESS_USER1))
