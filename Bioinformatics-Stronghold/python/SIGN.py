# Enumerating Oriented Gene Orderings
# https://rosalind.info/problems/sign/

from argparse import ArgumentParser


parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())


def generate_signed_permutations(n: int = N):

    def helper(perms, remaining):
        if not remaining:
            yield perms
        else:
            for i in remaining:
                yield from helper(perms + [-i], remaining - {i})
                yield from helper(perms + [i], remaining - {i})

    if n % 2 == 0:
        yield from helper([], set(range(1, n + 1)))
    else:
        for sign in [1, -1]:
            yield from helper([], set(range(1, n)) | {-n})


permutations = list(generate_signed_permutations())
output = f"{len(permutations)}\n"


for perm in permutations:
    output += " ".join([str(number) for number in perm]) + "\n"


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
