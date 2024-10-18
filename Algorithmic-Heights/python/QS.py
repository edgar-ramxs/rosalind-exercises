# Quick Sort
# https://rosalind.info/problems/qs/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_qs.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def QuickSort(arr):
    elements = len(arr)
    if elements < 2:
        return arr
    current_position = 0
    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp
    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp
    left = QuickSort(arr[0:current_position])
    right = QuickSort(arr[current_position + 1 : elements])
    arr = left + [arr[current_position]] + right
    return arr


B = A.copy()
quickSort(B, 0, N - 1)
# print(B)

# C = A.copy()
# C = quick_sort(C)
# print(C)

# D = A.copy()
# D = QuickSort(D)
# print(D)

OUTPUT = " ".join(map(str, B))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
