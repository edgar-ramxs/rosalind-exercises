# 2-Way Partition
# https://rosalind.info/problems/par/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_par.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def two_way_partition(a: list = A, n: int = N) -> list:
    array = a.copy()
    lamda, p, q = array[0], 1, n - 1

    while p <= q:
        if array[p] > lamda:
            array[p], array[q] = array[q], array[p]
            q -= 1
        else:
            array[p - 1] = array[p]
            p += 1

    array[p - 1] = lamda
    return array


OUTPUT = " ".join(map(str, two_way_partition(A)))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
