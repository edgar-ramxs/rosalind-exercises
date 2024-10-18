# Merge Two Sorted Arrays
# https://rosalind.info/problems/mer/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_mer.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    M = int(file.readline().strip())
    B = list(map(int, file.readline().split()))


def merge_arrays(array1: list = A, array2: list = B) -> list:
    return sorted(array1 + array2)


OUTPUT = " ".join(map(str, merge_arrays()))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
