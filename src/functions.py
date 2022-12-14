import time
import random
from Svar import *
import sys

bosslista = [] # En lista för boss_room
head = 0  # global variabel
key = False #Variabel för nyckeln i math_room


def tid():  # Funktion för att göra det snyggare
    """Funktion för att koden ska "stanna" en stund"""
    time.sleep(z)  # Väntar 2 sekunder

def val_av_tid():
    """Funktion för att välja tid"""
    global z
    print("Do you want to play fast, medium or slow?")
    print("1. Fast")
    print("2. Medium")
    print("3. Slow")
    tiden = input("> ")
    if tiden == "1":
        z = 0.5
    elif tiden == "2":
        z = 1.0
    elif tiden == "3":
        z = 1.5
    else:
        print("You did not choose a number.")
        tid()
        val_av_tid()



def sortera(bosslista):  # Funktion för att sortera listan
    """Funktion för att manuellt sortera en eller flera lisor"""
    for num in range(len(bosslista) - 1, 0, -1):  # num går från längden av bosslista - 1 till 0 med -1
        for idx in range(num):  # idx går från 0 till num
            if bosslista[idx] > bosslista[idx + 1]:  # om bosslista[idx] är större än bosslista[idx + 1]
                temp = bosslista[idx]  # temp är lika med bosslista[idx]
                bosslista[idx] = bosslista[idx + 1]  # bosslista[idx] är lika med bosslista[idx + 1]
                bosslista[idx + 1] = temp  # bosslista[idx + 1] är lika med temp
    return bosslista  # returnerar bosslista


def caps(text):
    """Funktion för att göra texten till versaler"""
    return text[0].upper() + text[1:].lower()


def animate():
    """Animerar en "loading bar" """
    print("Loading:")

    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]  # En lista med olika animationer

    for i in range(len(animation)):  # En for loop som går igenom listan
        time.sleep(0.5)  # Väntar 0.5 sekunder

        sys.stdout.write("\r" + animation[i % len(animation)])  # Skriver ut animationen
        sys.stdout.flush()  # Tar bort allt som är i sys.stdout
    print("\n")  # Skriver ut en ny rad


def Karaktar():
    """Funktion för att skapa karaktär"""
    while True:
        print("You can choose from 2 characters. John, Amy")
        ch = caps(input("Choose a character: "))
        if ch == "John":
            print("You have chosen John.")
            animate()
            with open("character.txt", "w") as f:
                f.write(ch)
            break
        elif ch == "Amy":
            print("You have chosen Amy.")
            animate()
            with open("character.txt", "w") as f:
                f.write(ch)
                break
        else:
            print("You did not choose a character.")
            animate()
            tid()
            continue


def dragon_room():
    """Funktion för drak rummet"""
    animate()
    print("You are in a room with a dragon.")
    tid()
    print("The dragon is sleeping.")
    tid()
    print("Do you want to take the gold or wake the dragon? (gold or dragon)")
    tid()
    choice = caps(input("> "))
    if choice == 'Gold':
        animate()
        print("You got the gold and ran away.")
        tid()
        blackroom()
    elif choice == 'Dragon':
        animate()
        dead("The dragon wakes up and eats you.")
    else:
        dead("You stumble around the room until you starve.")


def cthulhu_room():
    """Funktion för cthulhu rummet"""
    global head
    print("Here you see the great evil Cthulhu.")
    tid()
    print("He eats whatever stares at him and goes insane.")
    tid()
    print("What do you do?")
    tid()
    print("""
    a. Flee for your life
    b. Eat your head
    c. hit cathulu
    d. take cathulu's head
    e. smash cathulu
    f. kill cathulu
    """)
    tid()
    choice = caps(input("> "))
    if choice == 'A':
        print("You fleed to the black room.")
        blackroom()
    elif choice == 'B':
        print("You ate your head and died.")
        dead("You are dead.")
    elif choice == 'C':
        dead("Cathulu eats you.")
    elif choice == 'D':
        print("You took cathulu's head and ran away.")
        head += 1
        with open("head.txt", "w") as f:  # Öppnar head.txt och skriver över allt som står i filen
            f.write(str(head))  # Skriver in head i filen
        tid()
        print("You ran to another galaxy.")
        tid()
        blackroom()
    elif choice == 'E':
        dead("Cathulu eats your arms off.")
    elif choice == 'F':
        print("you killed cathulu and ran away.")
        tid()
        blackroom()
    else:
        dead("You stumble around the room until you starve.")


def bear_room():
    """Funktion för björn rummet"""
    global bear, bear_moved
    print("There is a bear here.")
    tid()
    print("The bear has a bunch of honey.")
    tid()
    print("The fat bear is in front of another door.")
    tid()
    print("Are you going to move the bear? (yes or no)")
    choice = caps(input("> "))
    if choice == 'No':
        blackroom()
    elif choice == 'Yes':
        print("How are you going to move the bear? Take honey or taunt bear? (take or taunt)")
        bear_moved = random.choice([True, False])  # Tar fram ett random värde mellan True och False
        bear = True
    else:
        dead("You stumble around the room until you starve.")

    while bear:
        choice = caps(input("> "))

        if choice == 'Take':
            dead("The bear looks at you then slaps your face off.")
            break
        elif choice == 'Taunt' and bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now or go back. (go or back)")
            choice = caps(input("> "))
            if choice == 'Go':
                blackroom()
            elif choice == 'Back':
                blackroom()
        elif choice == 'Taunt' and not bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
            break
        else:
            print("I got no idea what that means.")


def gold_room():
    """This is the gold room"""
    global choice, how_much
    print("This room is full of gold.  How much do you take? (numbers only)")

    try:  # Försöker köra koden
        choice = int(input("> "))
    except ValueError:
        dead("Death is the only answer.")  # Om det inte går att göra om till int så körs denna kod
    if isinstance(choice, int):
        how_much = int(choice)  # om choice är int kör den vidare
    else:
        dead("Death is the only answer.")

    if how_much <= 50:  # Om how_much är mindre eller lika med 50
        print("Nice, you're not greedy, you win!")
        victoryroom()
    else:
        dead("You greedy bastard!")


def dead(why):
    """Funktion som körs när du är död"""
    print("You died because: ", why, "Good job!")
    print("Do you want to play again? Y/N")
    choice = caps(input("> "))
    if choice == 'Y':
        back_to_start()
    elif choice == 'N':
        sys.exit(0)
    else:
        sys.exit(0)


def save_name():
    """Funktion för att spara namn"""
    namn = input("Write your name: ")
    with open("save.txt", "w") as f:
        f.write(namn)


def mathroom():
    """Funktion för matte rummet"""
    global key
    tries = {"John": 3, "Amy": 3}  # En dictionary med namn och antal försök

    rights = {"John": 0, "Amy": 0}  # En dictionary med namn och rätt svar

    with open("character.txt", "r") as f:  # Öppnar character.txt och läser innehållet
        karaktar = f.read()  # Läser innehållet i karaktär

    print("In this room you have to solve a math problem.")
    tid()
    print("You have 3 tries.")
    while karaktar == "John" or karaktar == "Amy":  # Om karaktär är John eller Amy
        tid()
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'What is {num1} + {num2}?')  # Skriver ut num1 och num2
        tid()
        flag = True  # Sätter flag till True
        answer = 0
        while flag:  # Så länge flag är True
            try:  # Försöker köra koden
                answer = int(input("> "))  # Tar in svaret
                flag = False  # Sätter flag till False
            except ValueError:  # Om det inte går att göra om till int så körs denna kod
                print("You have to write a number.")  # Skriver ut texten
        if answer == num1 + num2:  # Om svaret är rätt och answer är int
            rights[karaktar] += 1  # Lägger till 1 i rights
            with open("rights.txt", "w") as f:
                f.write(str(rights[karaktar]))  # Skriver in rights i filen
            print("You got it right.")
            tid()
            if tries[karaktar] == 0:
                dead("You ran out of tries.")
            elif rights[karaktar] == 3 and tries[karaktar] == 3:
                key = True
                print("Welcome to next room!")
                funroom()
            elif rights[karaktar] == 3 and tries[karaktar] < 3:
                print("Welcome to next room!")
                funroom()
            print("Next math problem.")
            tid()
        elif answer != num1 + num2:
            tries[karaktar] -= 1
            print("Wrong answer.")
            tid()
            print("Next math problem.")
            if tries[karaktar] == 0:
                dead("You ran out of tries.")
            elif rights[karaktar] == 3:
                print("Welcome to next room!")
                funroom()


def funroom():
    """Funktion för roliga rummet"""
    global key
    lista = []
    with open("character.txt", "r") as f:
        karaktar = f.read()
    print("In this room you have to guess a number.")
    tid()
    while karaktar == "John" or karaktar == "Amy":
        tid()
        num = random.randint(1, 5)
        lista.append(num)
        if key:
            print("You got the key.")
            print(f"The number is: {lista}")
        print("Guess a number between 1-5.")
        answer = int(input("> "))
        if answer == num:
            tid()
            print("You got it right.")
            tid()
            bossroom()
        elif answer != num:
            tid()
            print("Wrong answer.")


def bossroom():
    """Funktion för boss rummet"""
    global bosslista
    print("in this room you have to fight the boss. (aka me)")
    x = int(input("How many numbers do you want?: "))
    bosslista = [random.randint(1, 1000) for i in range(x)]  # En lista med x slumpmässiga tal mellan 1 och 1000 används i funktionen bossroom

    tid()
    print("The numbers are:", bosslista)
    svarlista = []
    sortera(bosslista)
    for i in range(x):
        svarlista.append(int(input("Write in the right order, one number at a time: ")))
    if svarlista == sortera(bosslista):  # Om bosslistan är lika med svarlistan
        print("You won!")
        gold_room()
    else:
        dead("You lost.")




def victoryroom():
    """Funktion för vinnar rummet"""
    print("You won the game.")
    tid()
    print("Do you want to play again? Y/N")
    choice = caps(input("> "))
    if choice == "Y":
        return
    elif choice == "N":
        sys.exit(0)
    else:
        sys.exit(0)


def blackroom():
    """Funktion för svart rummet"""
    print("You are in a black room.")
    tid()
    print("There are 3 doors.")
    tid()
    print("Which door do you want to go through? (1, 2 or 3)")
    tid()
    choice = caps(input("> "))
    if choice == '1':
        mathroom()
    elif choice == '2':
        mathroom()
    elif choice == '3':
        mathroom()
    else:
        dead("You stumble around the room until you starve.")


def back_to_start():
    """Funktion för att återgå till början"""
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
