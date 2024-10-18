# Rabbits and Recurrence Relations
# https://rosalind.info/problems/fib/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N, K = map(int, file.read().strip().split())


def dynamic_programing(months: int, rabbits_produces: int) -> int:
    if months == 0:
        return 0
    elif months == 1:
        return 1
    else:
        generations = [0] * (months + 1)
        generations[0] = 0
        generations[1] = 1

        for i in range(2, months + 1):
            generations[i] = generations[i - 1] + (
                generations[i - 2] * rabbits_produces
            )

        return generations[months]


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(dynamic_programing(N, K)))
