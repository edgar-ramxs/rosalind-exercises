# Building a Heap
# https://rosalind.info/problems/hea/


## INFO:
# https://www.youtube.com/watch?v=B7hVxCmfPtM
# https://www.geeksforgeeks.org/building-heap-from-array/
# https://medium.com/edureka/data-structures-algorithms-in-java-d27e915db1c5


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_hea.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def building_a_max_heap(array: list = A, n: int = N):
    for i in range(n - 1, 0, -1):
        parent = (i - 1) // 2
        if array[i] > array[parent]:
            array[parent], array[i] = array[i], array[parent]
            v = i
            while True:
                max_node = v
                if v * 2 + 1 < len(array) and array[v * 2 + 1] > array[max_node]:
                    max_node = v * 2 + 1
                if v * 2 + 2 < len(array) and array[v * 2 + 2] > array[max_node]:
                    max_node = v * 2 + 2
                if max_node == v:
                    break
                array[v], array[max_node] = array[max_node], array[v]
                v = max_node


building_a_max_heap()
OUTPUT = " ".join(map(str, A))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
