# 2SUM
# https://rosalind.info/problems/2sum/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_2sum.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K, N = list(map(int, file.readline().strip().split()))
    ARRAYS = []

    for line in file:
        arr = list(map(int, line.strip().split()))
        ARRAYS.append(arr)


def two_sum2(arrays: list = ARRAYS) -> str:
    
    def find_pairs(array: list) -> str:
        result = {}
        for index, value in enumerate(array):
            opposite = -value
            if opposite in result:
                return f"{result[opposite] + 1} {index + 1}"
            else:
                result[value] = index
        return "-1"

    output = ""
    for array in arrays:
        output += f"{find_pairs(array)}\n"
    return output


OUTPUT = two_sum2()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
