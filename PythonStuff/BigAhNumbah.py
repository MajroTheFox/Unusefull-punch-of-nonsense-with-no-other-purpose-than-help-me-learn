userChoice = input("You wanna encrypt or decrypt? (e/d): ")
if userChoice == "e":
    msgInt = int(input("Gimme the number you wanna hide: "))
    keyInt = int(input("Now gimme the key: "))
    nonsense = msgInt * keyInt
    print("This is your punch of nonsense: ")
    print(nonsense)
elif userChoice == "d":
    nonsense = int(input("Gimme the number you wanna decrypt: "))
    keyInt = int(input("Now gimme the key: "))
    msgInt = int(nonsense / keyInt)
    print("This is your punch of message: ")
    print(msgInt)
else:
    print("You were supossed to chose either e or d. What is wrong with you?")
