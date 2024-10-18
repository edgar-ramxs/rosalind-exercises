# Enumerating Gene Orders
# https://rosalind.info/problems/perm/

from argparse import ArgumentParser


parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())


def generate_permutations(n: int = N):
    permutations = []

    def backtrack(nums, path):
        if len(path) == n:
            permutations.append(path)
            return
        for num in nums:
            if num not in path:
                backtrack(nums, path + [num])

    if n <= 7:
        nums = list(range(1, n + 1))
        backtrack(nums, [])

        return permutations


permutations = generate_permutations()
output = f"{len(permutations)}\n"


for perm in permutations:
    output += " ".join([str(number) for number in perm]) + "\n"


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
