def TextToNumber(Text):    #This does not support the " character.
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


def NumberToText(Number):
    Text = ""
    if len(Number) % 2 == 0:
        for i in range(int(len(Number)/2)):
            if Number[i * 2] == "0":
                if Number[i * 2 + 1] == "0":
                    Text += "0"
                elif Number[i * 2 + 1] == "1":
                    Text += "1"
                elif Number[i * 2 + 1] == "2":
                    Text += "2"
                elif Number[i * 2 + 1] == "3":
                    Text += "3"
                elif Number[i * 2 + 1] == "4":
                    Text += "4"
                elif Number[i * 2 + 1] == "5":
                    Text += "5"
                elif Number[i * 2 + 1] == "6":
                    Text += "6"
                elif Number[i * 2 + 1] == "7":
                    Text += "7"
                elif Number[i * 2 + 1] == "8":
                    Text += "8"
                elif Number[i * 2 + 1] == "9":
                    Text += "9"
            elif Number[i * 2] == "1":
                if Number[i * 2 + 1] == "0":
                    Text += "A"
                elif Number[i * 2 + 1] == "1":
                    Text += "B"
                elif Number[i * 2 + 1] == "2":
                    Text += "C"
                elif Number[i * 2 + 1] == "3":
                    Text += "D"
                elif Number[i * 2 + 1] == "4":
                    Text += "E"
                elif Number[i * 2 + 1] == "5":
                    Text += "F"
                elif Number[i * 2 + 1] == "6":
                    Text += "G"
                elif Number[i * 2 + 1] == "7":
                    Text += "H"
                elif Number[i * 2 + 1] == "8":
                    Text += "I"
                elif Number[i * 2 + 1] == "9":
                    Text += "J"
            elif Number[i * 2] == "2":
                if Number[i * 2 + 1] == "0":
                    Text += "K"
                elif Number[i * 2 + 1] == "1":
                    Text += "L"
                elif Number[i * 2 + 1] == "2":
                    Text += "M"
                elif Number[i * 2 + 1] == "3":
                    Text += "N"
                elif Number[i * 2 + 1] == "4":
                    Text += "O"
                elif Number[i * 2 + 1] == "5":
                    Text += "P"
                elif Number[i * 2 + 1] == "6":
                    Text += "Q"
                elif Number[i * 2 + 1] == "7":
                    Text += "R"
                elif Number[i * 2 + 1] == "8":
                    Text += "S"
                elif Number[i * 2 + 1] == "9":
                    Text += "T"
            elif Number[i * 2] == "3":
                if Number[i * 2 + 1] == "0":
                    Text += "U"
                elif Number[i * 2 + 1] == "1":
                    Text += "V"
                elif Number[i * 2 + 1] == "2":
                    Text += "W"
                elif Number[i * 2 + 1] == "3":
                    Text += "X"
                elif Number[i * 2 + 1] == "4":
                    Text += "Y"
                elif Number[i * 2 + 1] == "5":
                    Text += "Z"
                elif Number[i * 2 + 1] == "6":
                    Text += "a"
                elif Number[i * 2 + 1] == "7":
                    Text += "b"
                elif Number[i * 2 + 1] == "8":
                    Text += "c"
                elif Number[i * 2 + 1] == "9":
                    Text += "d"
            elif Number[i * 2] == "4":
                if Number[i * 2 + 1] == "0":
                    Text += "e"
                elif Number[i * 2 + 1] == "1":
                    Text += "f"
                elif Number[i * 2 + 1] == "2":
                    Text += "g"
                elif Number[i * 2 + 1] == "3":
                    Text += "h"
                elif Number[i * 2 + 1] == "4":
                    Text += "i"
                elif Number[i * 2 + 1] == "5":
                    Text += "j"
                elif Number[i * 2 + 1] == "6":
                    Text += "k"
                elif Number[i * 2 + 1] == "7":
                    Text += "l"
                elif Number[i * 2 + 1] == "8":
                    Text += "m"
                elif Number[i * 2 + 1] == "9":
                    Text += "n"
            elif Number[i * 2] == "5":
                if Number[i * 2 + 1] == "0":
                    Text += "o"
                elif Number[i * 2 + 1] == "1":
                    Text += "p"
                elif Number[i * 2 + 1] == "2":
                    Text += "q"
                elif Number[i * 2 + 1] == "3":
                    Text += "r"
                elif Number[i * 2 + 1] == "4":
                    Text += "s"
                elif Number[i * 2 + 1] == "5":
                    Text += "t"
                elif Number[i * 2 + 1] == "6":
                    Text += "u"
                elif Number[i * 2 + 1] == "7":
                    Text += "v"
                elif Number[i * 2 + 1] == "8":
                    Text += "w"
                elif Number[i * 2 + 1] == "9":
                    Text += "x"
            elif Number[i * 2] == "6":
                if Number[i * 2 + 1] == "0":
                    Text += "y"
                elif Number[i * 2 + 1] == "1":
                    Text += "z"
                elif Number[i * 2 + 1] == "2":
                    Text += "!"
                elif Number[i * 2 + 1] == "3":
                    Text += "#"
                elif Number[i * 2 + 1] == "4":
                    Text += "$"
                elif Number[i * 2 + 1] == "5":
                    Text += "%"
                elif Number[i * 2 + 1] == "6":
                    Text += "&"
                elif Number[i * 2 + 1] == "7":
                    Text += "'"
                elif Number[i * 2 + 1] == "8":
                    Text += "("
                elif Number[i * 2 + 1] == "9":
                    Text += ")"
            elif Number[i * 2] == "7":
                if Number[i * 2 + 1] == "0":
                    Text += "*"
                elif Number[i * 2 + 1] == "1":
                    Text += "+"
                elif Number[i * 2 + 1] == "2":
                    Text += ","
                elif Number[i * 2 + 1] == "3":
                    Text += "-"
                elif Number[i * 2 + 1] == "4":
                    Text += "."
                elif Number[i * 2 + 1] == "5":
                    Text += "/"
                elif Number[i * 2 + 1] == "6":
                    Text += ":"
                elif Number[i * 2 + 1] == "7":
                    Text += ";"
                elif Number[i * 2 + 1] == "8":
                    Text += "<"
                elif Number[i * 2 + 1] == "9":
                    Text += "="
            elif Number[i * 2] == "8":
                if Number[i * 2 + 1] == "0":
                    Text += ">"
                elif Number[i * 2 + 1] == "1":
                    Text += "?"
                elif Number[i * 2 + 1] == "2":
                    Text += "@"
                elif Number[i * 2 + 1] == "3":
                    Text += "["
                elif Number[i * 2 + 1] == "4":
                    Text += "[a slash turned the other way]"
                elif Number[i * 2 + 1] == "5":
                    Text += "]"
                elif Number[i * 2 + 1] == "6":
                    Text += "^"
                elif Number[i * 2 + 1] == "7":
                    Text += "_"
                elif Number[i * 2 + 1] == "8":
                    Text += "`"
                elif Number[i * 2 + 1] == "9":
                    Text += "{"
            elif Number[i * 2] == "9":
                if Number[i * 2 + 1] == "0":
                    Text += "|"
                elif Number[i * 2 + 1] == "1":
                    Text += "}"
                elif Number[i * 2 + 1] == "2":
                    Text += "~"
                elif Number[i * 2 + 1] == "3":
                    Text += "€"
                elif Number[i * 2 + 1] == "4":
                    Text += "‰"
                elif Number[i * 2 + 1] == "5":
                    Text += "•"
                elif Number[i * 2 + 1] == "6":
                    Text += "µ"
                elif Number[i * 2 + 1] == "7":
                    Text += "‡"
                elif Number[i * 2 + 1] == "8":
                    Text += " "
                elif Number[i * 2 + 1] == "9":
                    Text += "[UNKNOWN CHARACTER]"
    else:
        Text = "An error occured. Number must have an even number of diggits."
    return Text
print(TextToNumber(input("Input Text: ")))
print(NumberToText(str(input("Input number: "))))