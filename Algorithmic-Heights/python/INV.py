# Counting Inversions
# https://rosalind.info/problems/inv/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_inv.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def counting_inversions1(array: list = A):

    def merge(left: list, right: list):
        result = []
        inversions = 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inversions += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions

    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left, left_inv = counting_inversions1(array[:mid])
    right, right_inv = counting_inversions1(array[mid:])
    merged, inversions = merge(left, right)
    return merged, inversions + left_inv + right_inv


def counting_inversions2(A):

    def merge(left, right):
        merged = []
        inversions = 0
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
        merged += left[i:]
        merged += right[j:]
        return merged, inversions

    def merge_sort(A):
        if len(A) <= 1:
            return A, 0

        mid = len(A) // 2
        left, left_inversions = merge_sort(A[:mid])
        right, right_inversions = merge_sort(A[mid:])
        merged, merge_inversions = merge(left, right)
        return merged, left_inversions + right_inversions + merge_inversions

    _, inversions = merge_sort(A)
    return inversions


OUTPUT = str(counting_inversions1(A)[1])
# OUTPUT = str(counting_inversions2(A))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
