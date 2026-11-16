def TextToNumber(Text):
    Number = ""
    for i in range(len(Text)):
        if Text[i] == "1":
            Number += "01"
        elif Text[i] == "2":
            Number += "02"
        elif Text[i] == "3":
            Number += "03"
        elif Text[i] == "4":
            Number += "04"
        elif Text[i] == "5":
            Number += "05"
        elif Text[i] == "6":
            Number += "06"
        elif Text[i] == "7":
            Number += "07"
        elif Text[i] == "8":
            Number += "08"
        elif Text[i] == "9":
            Number += "09"
        elif Text[i] == "A":
            Number += "10"
        elif Text[i] == "B":
            Number += "11"
        elif Text[i] == "C":
            Number += "12"
        elif Text[i] == "D":
            Number += "13"
        elif Text[i] == "E":
            Number += "14"
        elif Text[i] == "F":
            Number += "15"
        elif Text[i] == "G":
            Number += "16"
        elif Text[i] == "H":
            Number += "17"
        elif Text[i] == "I":
            Number += "18"
        elif Text[i] == "J":
            Number += "19"
        elif Text[i] == "K":
            Number += "20"
        elif Text[i] == "L":
            Number += "21"
        elif Text[i] == "M":
            Number += "22"
        elif Text[i] == "N":
            Number += "23"
        elif Text[i] == "O":
            Number += "24"
        elif Text[i] == "P":
            Number += "25"
        elif Text[i] == "Q":
            Number += "26"
        elif Text[i] == "R":
            Number += "27"
        elif Text[i] == "S":
            Number += "28"
        elif Text[i] == "T":
            Number += "29"
        elif Text[i] == "U":
            Number += "30"
        elif Text[i] == "V":
            Number += "31"
        elif Text[i] == "W":
            Number += "32"
        elif Text[i] == "X":
            Number += "33"
        elif Text[i] == "Y":
            Number += "34"
        elif Text[i] == "Z":
            Number += "35"
        elif Text[i] == "a":
            Number += "36"
        elif Text[i] == "b":
            Number += "37"
        elif Text[i] == "c":
            Number += "38"
        elif Text[i] == "d":
            Number += "39"
        elif Text[i] == "e":
            Number += "40"
        elif Text[i] == "f":
            Number += "41"
        elif Text[i] == "g":
            Number += "42"
        elif Text[i] == "h":
            Number += "43"
        elif Text[i] == "i":
            Number += "44"
        elif Text[i] == "j":
            Number += "45"
        elif Text[i] == "k":
            Number += "46"
        elif Text[i] == "l":
            Number += "47"
        elif Text[i] == "m":
            Number += "48"
        elif Text[i] == "n":
            Number += "49"
        elif Text[i] == "o":
            Number += "50"
        elif Text[i] == "p":
            Number += "51"
        elif Text[i] == "q":
            Number += "52"
        elif Text[i] == "r":
            Number += "53"
        elif Text[i] == "s":
            Number += "54"
        elif Text[i] == "t":
            Number += "55"
        elif Text[i] == "u":
            Number += "56"
        elif Text[i] == "v":
            Number += "57"
        elif Text[i] == "w":
            Number += "58"
        elif Text[i] == "x":
            Number += "59"
        elif Text[i] == "y":
            Number += "60"
        elif Text[i] == "z":
            Number += "61"
        elif Text[i] == "!":
            Number += "62"
        elif Text[i] == "#":
            Number += "63"
        elif Text[i] == "$":
            Number += "64"
        elif Text[i] == "%":
            Number += "65"
        elif Text[i] == "&":
            Number += "66"
        elif Text[i] == "'":
            Number += "67"
        elif Text[i] == "(":
            Number += "68"
        elif Text[i] == ")":
            Number += "69"
        elif Text[i] == "*":
            Number += "70"
        elif Text[i] == "+":
            Number += "71"
        elif Text[i] == ",":
            Number += "72"
        elif Text[i] == "-":
            Number += "73"
        elif Text[i] == ".":
            Number += "74"
        elif Text[i] == "/":
            Number += "75"
        elif Text[i] == ":":
            Number += "76"
        elif Text[i] == ";":
            Number += "77"
        elif Text[i] == "<":
            Number += "78"
        elif Text[i] == "=":
            Number += "79"
        elif Text[i] == ">":
            Number += "80"
        elif Text[i] == "?":
            Number += "81"
        elif Text[i] == "@":
            Number += "82"
        elif Text[i] == "[":
            Number += "83"
#        elif Text[i] == "[a slash turned the other way]":  #This one does not work (for obvious reasons).
#            Number += "84"
        elif Text[i] == "]":
            Number += "85"
        elif Text[i] == "^":
            Number += "86"
        elif Text[i] == "_":
            Number += "87"
        elif Text[i] == "`":
            Number += "88"
        elif Text[i] == "{":
            Number += "89"
        elif Text[i] == "|":
            Number += "90"
        elif Text[i] == "}":
            Number += "91"
        elif Text[i] == "~":
            Number += "92"
        elif Text[i] == "€":
            Number += "93"
        elif Text[i] == "‰":
            Number += "94"
        elif Text[i] == "•":
            Number += "95"
        elif Text[i] == "µ":
            Number += "96"
        elif Text[i] == "‡":
            Number += "97"
        elif Text[i] == " ":
            Number += "98"
        else:
            Number += "99"
    return Number
print(TextToNumber(input("Input number: ")))