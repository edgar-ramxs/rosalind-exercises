# 3-Way Partition
# https://rosalind.info/problems/par3/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_par3.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def three_way_partition(array: list = A, n: int = N) -> None:
    pivot = array[0]
    leftLess, left, right, rightGreater = 0, 0, n - 1, n - 1

    while left <= right:

        while left <= right and array[left] <= pivot:
            if array[left] < pivot:
                array[leftLess], array[left] = array[left], array[leftLess]
                leftLess += 1
            left += 1
        array[left], array[right] = array[right], array[left]

        while left <= right and array[right] >= pivot:
            if array[right] > pivot:
                array[right], array[rightGreater] = array[rightGreater], array[right]
                rightGreater -= 1
            right -= 1
        array[left], array[right] = array[right], array[left]


three_way_partition()
OUTPUT = " ".join(map(str, A))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
