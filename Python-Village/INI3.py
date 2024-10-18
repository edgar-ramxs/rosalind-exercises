# Strings and Lists
# https://rosalind.info/problems/ini3/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
#
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ini3.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"


with open(PATH_INPUT, "r") as file:
    TEXT = file.readline().rstrip()
    A, B, C, D = list(map(int, file.readline().strip().split()))


OUTPUT = f"{TEXT[A:B+1]} {TEXT[C:D+1]}"


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
