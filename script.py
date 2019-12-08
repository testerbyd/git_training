#!/usr/bin/python

import sys
import os.path

def has_number(string):
    return any(char.isdigit() for char in string)

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = "lorem.txt"

if os.path.exists(file_name):
    if os.path.isfile(file_name):

        file = open(file_name, "r")

        lines = file.readlines()
        lines = [line.strip() for line in lines]

        file.close()

        print("The lines which contain numbers:\n")

        for line in lines:
            if has_number(line):
                print(line)


        print("Lenghts of lines:\n")

        for line in lines:
            print(len(line))

        line_length = int(raw_input("Please give me a length of the lines you want to print: "))

        for line in lines:
            if len(line) == line_length:
                print(line)
                
        word_to_find = raw_input("Please give me a word you want to find: ")

        lines_count = 0

        for line in lines:
            if word_to_find in line:
                lines_count = lines_count + 1

        print("The word " + word_to_find + " occurs " + str(lines_count) + " times") 

    else:
        print(file_name + " is not a file.")
else:
    print("File " + file_name + " does not exist.")
