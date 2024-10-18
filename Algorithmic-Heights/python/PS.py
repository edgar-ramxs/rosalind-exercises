# Partial Sort
# https://rosalind.info/problems/ps/


## INFO:
# https://dev.to/dottt/sorting-algorithm-with-python-code-ilo
# https://en.wikipedia.org/wiki/Partial_sorting


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ps.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    K = int(file.readline().strip())


def merge_sort(array: list = A):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


merge_sort()
OUTPUT = " ".join(map(str, A[:K]))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
