# Binary Search
# https://rosalind.info/problems/bins/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_bins.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    M = int(file.readline().strip())
    An = list(map(int, file.readline().strip().split()))  # ListOrder
    Bm = list(map(int, file.readline().strip().split()))  # ListElement


def binary_search(array: list, k: int) -> int:
    start = 0
    middle = None
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        if array[middle] < k:
            start = middle + 1
        elif array[middle] > k:
            end = middle - 1
        else:
            return middle

    return -1


def searching_elements(ListOrder: list = An, ListElement: list = Bm) -> str:
    output = ""
    for k in ListElement:
        positionElement = binary_search(ListOrder, k)
        output += f"{ positionElement + 1  if positionElement >= 0 else positionElement} "
    return output


OUTPUT = searching_elements()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
