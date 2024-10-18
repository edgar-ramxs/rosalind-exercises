# Median
# https://rosalind.info/problems/med/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_med.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################


with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    K = int(file.readline().strip())


import random


def kth_smallest_element1(arr: list = A, k: int = K):

    def partition(arr, low, high):
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def random_select(arr, low, high, k):
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        length_left = pivot_index - low + 1
        if k == length_left:
            return arr[pivot_index]
        elif k < length_left:
            return random_select(arr, low, pivot_index - 1, k)
        else:
            return random_select(arr, pivot_index + 1, high, k - length_left)

    return random_select(arr, 0, len(arr) - 1, k)


def kth_smallest_element2(A: list, p: int, r: int, k: int):
    if p == r:
        return A[p]

    q = random.randint(p, r)
    A[p], A[q] = A[q], A[p]

    i = p + 1
    for j in range(p + 1, r + 1):
        if A[j] < A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[p], A[i - 1] = A[i - 1], A[p]

    if k == i - p:
        return A[i - 1]
    elif k < i - p:
        return kth_smallest_element2(A, p, i - 2, k)
    else:
        return kth_smallest_element2(A, i, r, k - (i - p))


OUTPUT = str(kth_smallest_element1())
# OUTPUT = str(kth_smallest_element2(A, 0, N - 1, K))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
