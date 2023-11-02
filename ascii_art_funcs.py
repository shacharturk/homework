import re
import random
from typing import List


def find_max(lines):
    maximum = 0
    for x in lines:
        if len(x) > maximum:
            maximum = len(x)
    return maximum


def rotate(text, angle):
    def mirror(file_name):
        txt = open(file_name, "r")
        lines = list(txt.readlines())
        maximum = find_max(lines)
        txt.close()
        txt = open(file_name, "w")
        for i in lines:
            a = i[:len(i)-2] #i needed to remove the line break and than return it for it to work
            txt.write((maximum-len(a))*" " + a[::-1]+chr(10))
        txt.close()


    def rotation(file_name):  # text is the file's name, because we need it to both read and write in it
        txt = open(file_name, "r")
        lines = txt.readlines()
        txt.close()
        result = open("temporal.txt", "w")
        maximum = find_max(lines)
        rev = list(reversed(lines))
        rev = rev[1:] #i needed to remove the line break here too, and here it was at the beginning
        for j in range(0, maximum - 1):
            line = ""
            for i in rev:
                if j < len(i):
                    line += i[j]
                else:
                    line += " "
            result.write(line + chr(10))
        result.close()
        read = open("temporal.txt", "r")
        r = read.readlines()
        txt = open(file_name, "w")
        for i in r:
            txt.write(i)
        read.close()
        txt.close()

    if angle != 360:
        for x in range(int(angle / 90)):
            rotation(text)
    else:
        mirror(text)


def convert(file_name, table, conversion_index):
    if conversion_index != 0:
        file = open(file_name, "r")
        txt = file.readlines()
        file.close()
        temp, line = [], ""
        for x in txt:
            for y in x:
                if ord(y) == 10:
                    line += chr(10)
                elif y == " ":
                    line += " "
                elif y in table:
                    line += table[y][conversion_index - 1]
                else:
                    line += "x"
            temp += line
            line = ""
        result = open(file_name, "w")
        for x in temp:
            result.write(x)
        result.close()


def serialize(file_name):
    a = open("outcome.txt", "a")
    a.close()
    result = open("outcome.txt", "w")
    txt = open(file_name, "r")
    lines: list[str] = txt.readlines()
    txt.close()
    for x in lines:
        line, last = "", x[0]
        count, i = 0, 0
        # checking the nuber of identical characters in a row:
        while i < len(x)-1:
            if x[i] == last:
                count += 1
            # adding the final number with the character to the serialized string
            if x[i] != last or i == len(x) - 1:
                line += str(count)
                line += last
                count = 1
            last = x[i]
            i += 1
        result.write(line)
        result.write(chr(10))


def deserialize(file_name):
    text = open(file_name, "r")
    lines = list(text.readlines())
    text.close()
    result = open("outcome.txt", "w")
    for x in lines:
        x = re.split('(\D)', x)
        i = 0
        line = ""
        while x[i] != "":
            count = 0
            while count < int(x[i]):
                line += x[i + 1]
                count += 1
            i += 2
        result.write(line)
        result.write(chr(10))
        print("line: " + line)
    result.close()