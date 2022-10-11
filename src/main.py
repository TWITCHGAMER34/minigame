from functions import *
from Svar import *
import time

def tid(): #Tid
    time.sleep(2)


def main():
    while True:
        Karaktar()
        tid()
        save_name()
        tid()
        print("You are in a dark room.")
        tid()
        print("""
        There is a door in front of you which is red 
        to your right it is a door that is yellow 
        and to your left it is a door that is pink.
        """)
        tid()
        print("Which one do you take?")
        tid()
        print("Type 'red', 'yellow' or 'pink' and hit 'Enter'.")
        tid()
        choice = input("> ")
        if choice in svar_yellow:
            bear_room()
        elif choice in svar_red:
            cthulhu_room()
        elif choice in svar_pink:
            dragon_room()
        else:
            dead("You stumble around the room until you starve.")


if __name__ == "__main__": # Call main
    main()
