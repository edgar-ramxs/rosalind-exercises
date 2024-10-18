# Insertion Sort
# https://rosalind.info/problems/ins/


## INFO:
# https://www.toptal.com/developers/sorting-algorithms/insertion-sort
# https://en.wikipedia.org/wiki/Insertion_sort


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ins.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def insertion_sort(array: list = A, n_elements: int = N):
    swap = 0
    for i in range(1, n_elements):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            swap += 1
            j -= 1
    return swap


OUTPUT = str(insertion_sort())


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
