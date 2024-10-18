# Calculating Expected Offspring
# https://rosalind.info/problems/iev/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    DATA = list(map(int, file.readline().strip().split()))


def calculating_expected_offspring(couples: list = DATA, offspring_sons: int = 2) -> float:
    # IPRB.py -> prob
    # AA-AA = 1
    # AA-Aa = 1
    # AA-aa = 1
    # Aa-Aa = 0.75
    # Aa-aa = 0.5
    # aa-aa = 0
    PROB = [1, 1, 1, 3/4, 1/2, 0]
    return sum([x[0] * x[1] * offspring_sons for x in zip(couples, PROB)])


OUTPUT = str(calculating_expected_offspring())

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
