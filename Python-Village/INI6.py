# Dictionaries
# https://rosalind.info/problems/ini6/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
#
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ini6.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"


with open(PATH_INPUT, "r") as file:
    WORDS = file.readline().strip().split()
    OUTPUT = ""
    DICTIONARY = dict()


for word in WORDS:
    if not word in DICTIONARY:
        DICTIONARY[word] = 1
    else:
        DICTIONARY[word] += 1

for word, appearances in DICTIONARY.items():
    OUTPUT += f"{word} {appearances}\n"


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
