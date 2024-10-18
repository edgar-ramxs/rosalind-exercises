# Conditions and Loops
# https://rosalind.info/problems/ini4/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
#
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ini4.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"


with open(f"./inputs/{FILE_NAME}", "r") as file:
    A, B = list(map(int, file.readline().strip().split()))


OUTPUT = f"{sum(num for num in range(A, B) if num % 2 == 1)}"


with open(f"./outputs/output_{FILE_NAME}", "w") as output_file:
    output_file.write(OUTPUT)
