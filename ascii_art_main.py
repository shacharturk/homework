from ascii_art_funcs import serialize, deserialize, rotate, convert


#I didn't find any conversion table with the instructions, so I had to generate one
table = {"#" : ("(", "e"), "!" : ("G", "W"), "$" : ("G", "L"), "%" : ("b", "8"), "&" : ("p", "p"), "'" : ("Z", "8"), "(" : ("}", "z"), ")" : ("c", "n"), "*" : ("[", "*"), "+" : ("*", "_"), "," : ("+", "Q"), "-" : ("W", "~"), "." : ("E", "M"), "/" : ("L", "1"), ":" : ("$", ":"), ";" : ("z", "*"), " < " : ("!", ")"), "= " : (" ^ ", "."), " > " : (".", "H"), "?" : ("{", "P"), " @ " : ("e", "v"), "A" : ("a", "o"), "B" : (": ", "O"), "C" : ("N", ", "), "D" : ("3", "v"), "E" : (";", "["), "F" : ("X", "t"), "G" : (" & ", "!"), "H" : ("5", " & "), "I" : ("r", "w"), "J" : ("8", "k"), "K" : ("q", "]"), "L" : ("n", "H"), "M" : ("$", "B"), "N" : ("8", "a"), "O" : ("}", " < "), "P" : ("Z", "]"), "Q" : ("X", "0"), "R" : ("z", " ^ "), "S" : ("x", "c"), "T" : (" * ", "?"), "U" : ("H", "]"), "V" : ("{", " > "), "W" : ("M", " * "), "X" : ("`", "v"), "Y" : ("0", "6"), "Z" : ("c", "`"), "[" : ("D", "S"), "^" : ("k", ";"), "]" : ("(", "T"), " ^ " : ("G", "p"), "_" : ("5", "x"), "`" : ("b", "b"), "a" : (" & ", "w"), "b" : ("M", "s"), "c" : ("T", "I"), "d" : ("X", "w"), "e" : ("= ", "_"), "f" : ("b", "6"), "g" : ("c", " % "), "h" : ("L", "f"), "i" : (" + ", "`"), "j" : ("p", "X"), "k" : ("8", "x"), "l" : ("Q", "e"), "m" : ("S", "o"), "n" : ("P", "~"), "o" : ("?", "N"), "p" : ("!", "7"), "q" : ("@", "j"), "r" : ("Q", "i"), "s" : ("C", "r"), "t" : ("J", "Z"), "u" : ("#", "."), "v" : (":", "k"), "w" : ("[", "5"), "x" : ("D", "="), "y" : ("/", ":"), "z" : ("S", "S"), "{" : ("}", "c"), "|" : ("L", "p"), "}" : ("%", "7")}


action = str(input("would you like to serialize or deserialize (or none)?"))
if action != "serialize" and action != "deserialize" and action != "none":
    raise Exception('illegal input: inexisting action')
file_name = str(input("on which file would you like this action to be performed?"))
if file_name[len(file_name)-4:] != ".txt":
    raise Exception('illegal input: illegal file name')
angle = int(input("at what angle would you like to rotate your picture?"))
if angle != 0 and angle != 90 and angle != 180 and angle != 270 and angle != 360:
    raise Exception('illegal input: only angles allowed are 0, 90, 180, 270, 360')
conversion = int(input("would you like to convert the chars in your picture? (0,1,2)"))
if conversion != 0 and conversion != 1 and conversion != 2:
    raise Exception('illegal input: conversion nuber can only be 1, 2, 3')

if action == "serialize":
    serialize(file_name)
elif action == "deserialize":
    deserialize(file_name)
else:
    txt=open(file_name,"r")
    lines = txt.readlines()
    txt.close()
    result=open("outcome.txt","w")
    for x in lines:
        result.write(x)
    result.close()
rotate("outcome.txt", angle)

convert("outcome.txt", table, conversion)
print('the file name is "outcome.txt"')
result = open("outcome.txt", "r")
lines = result.readlines()
result.close()
for i in lines:
    print(i[:len(i)-2])
