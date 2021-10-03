import random

count = 0
number = 0
choice = ""
remain = 3

def right_or_wrong(x):
    global number
    if x == number:
        print("oh damm you won i will won next")
        fin(x)
    else:
        if x > number:
            print("your number is too high")
        else:
            print("your number is too low")
        contador()

def contador():
    global count
    global remain
    count += 1
    remain -= 1
    global choice
    if count < 3:
        print("wrong another try")
        print("you have " + str(remain) + " attemps less")
        choice = int(input("say your guess \n"))
        right_or_wrong(choice)
    else:
        fin(choice)

def fin(x):
    global count
    global remain
    count = 0
    remain = 3
    if number != x:
        print("looks like i won do you want a remacht \n y/n")
        re = input()
        re = re.lower()
        if re == "y":
            inicio()
        else:
            print("well i was fun, see you later")
    else:
        print("looks like i lose do you want a remacht \n y/n")
        re = input()
        re = re.lower()
        if re == "y":
            inicio()
        else:
            print("well i was fun, see you later")
def inicio():
    global number
    number = random.randint(1, 10)
    print("welcome to the guessing game!")
    print("ready i have my number between 1 and 10")
    choice = int(input("say your guess \n"))
    right_or_wrong(choice)

inicio()