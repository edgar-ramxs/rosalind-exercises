# Heap Sort
# https://rosalind.info/problems/hs/


## INFO:
# https://www.toptal.com/developers/sorting-algorithms/heap-sort
# https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
# https://www.geeksforgeeks.org/heap-sort/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_hs.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def heat_sort(array: list = A, n: int = N) -> None:

    def heapify(arr: list, N: int, i: int):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < N and arr[largest] < arr[l]:
            largest = l

        if r < N and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, N, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


heat_sort()
OUTPUT = " ".join(map(str, A))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
