# NUMBER CHOOSING SMALL GAME.

from smalqameans import *

def game():
    while True:
        try:
            num=input("Enter a number :")
            acpNum=int(num)
            if len(num)>2:
                print("choose only two digit number [1-99]")
            if acpNum == a:
                print("you have selected a correct number")
                break
            else:
                print("sorry,better luck next time")
                continue
        except Exception as e:
            print(e)
game()