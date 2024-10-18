# 3SUM
# https://rosalind.info/problems/3sum/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_3sum.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K, N = list(map(int, file.readline().split()))
    MATRIX = [list(map(int, line.split())) for line in file.readlines()]


def three_indices(arrays: list = MATRIX, k: int = K, n: int = N):
    output = ""
    for array in arrays:
        numbers = {}
        found = False
        for index in range(0, n):
            numbers[array[index]] = index
        for a in range(0, n):
            if found == True:
                break
            else:
                first = array[a]
            for b in range(a + 1, n):
                second = array[b]
                if ((-1) * (first + second)) in numbers:
                    c = numbers[(-1) * (first + second)]
                    output += f"{a+1} {b+1} {c+1}\n"
                    found = True
                    break
        if found == False:
            output += f"{-1}\n"
    return output


OUTPUT = three_indices()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
