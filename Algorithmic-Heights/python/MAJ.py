# Majority Element
# https://rosalind.info/problems/maj/


## INFO:
# Algoritmo de Boyer-Moore
# https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_de_cadenas_Boyer-Moore
# https://www.geeksforgeeks.org/majority-element/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_maj.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K, N = list(map(int, file.readline().strip().split()))
    ARRAYS = [list(map(int, line.rstrip().split(" "))) for line in file]


def majority_element_search(nums: list, n: int = N):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1


OUTPUT = ""
for array in ARRAYS:
    OUTPUT += f"{majority_element_search(array)} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
