
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
print(NumberToText(str(input("Zadaj cislo: "))))