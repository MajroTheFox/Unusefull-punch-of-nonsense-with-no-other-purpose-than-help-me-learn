continuenuenly = True
while continuenuenly:
    userChoice = input("You wanna encrypt or decrypt? (e/d): ")

    if userChoice == "e":
        message = str(input("Gimme what you want to hide from MOSSAD: "))
        keyInt = int(input("Now gimme the key: "))
        numbah = int.from_bytes(message.encode("utf-8"), "big")    #Half of this one was made by DeepSeek
        nonsense = numbah * keyInt
        print("This is your punch of nonsense: ")
        print(nonsense)
    elif userChoice == "d":
        nonsense = int(input("Gimme the punch of nonsense: "))
        keyInt = int(input("Now gimme the key: "))
        numbah = int(nonsense / keyInt)
        message = numbah.to_bytes((numbah.bit_length() + 7) // 8, "big").decode("utf-8")    #Half of this one was made by DeepSeek
        print("This is your punch of message: ")
        print(message)
    else:
        print("You were supossed to chose either e or d. What is wrong with you?")
    runAgain = input("Run again? (y/n): ")
    if runAgain == "y":
        print("Oki, running again!")
    elif runAgain == "n":
        print("Ok, bye!")
        continuenuenly = False
    else:
        print("WHAT ARE YOU DOING!? Do you want to break my code!? You are supossed to either input y or n! What is so hard to understand?")
        continuenuenly = False