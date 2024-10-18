# Longest Increasing Subsequence
# https://rosalind.info/problems/lgis/


from argparse import ArgumentParser


parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    PERMUTATION = list(map(int, file.readline().strip().split()))


def longest_increasing_subsequence(array: list = PERMUTATION) -> list:
    n = len(array)
    m = [1] * n  
    result = []
    max_length = 0

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j] and m[i] < m[j] + 1:
                m[i] = m[j] + 1
        max_length = max(max_length, m[i])

    for i in range(n - 1, -1, -1):
        if m[i] == max_length:
            result.append(array[i])
            max_length -= 1
            if max_length == 0:
                break

    return result[::-1]


def longest_decreasing_subsequence(array: list = PERMUTATION) -> list:
    n = len(array)
    m = [1] * n
    result = []
    max_length = 0

    for i in range(1, n):
        for j in range(i):
            if array[i] < array[j] and m[i] < m[j] + 1:
                m[i] = m[j] + 1
        max_length = max(max_length, m[i])

    for i in range(n - 1, -1, -1):
        if m[i] == max_length:
            result.append(array[i])
            max_length -= 1
            if max_length == 0:
                break

    return result[::-1]


output = " ".join(map(str, longest_increasing_subsequence()))
output += "\n"
output += " ".join(map(str, longest_decreasing_subsequence()))

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
