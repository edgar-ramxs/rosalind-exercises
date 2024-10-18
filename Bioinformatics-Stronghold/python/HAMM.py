# Counting Point Mutations
# https://rosalind.info/problems/hamm/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    S, T = file.read().strip().split()


# The Hamming distance
def counting_mutations(dna1: str, dna2: str) -> int:
    if len(dna1) != len(dna2):
        raise ValueError("Undefined for sequences of unequal length.")
    # return Dh
    return sum(char1 != char2 for char1, char2 in zip(dna1, dna2))


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(counting_mutations(S, T)))
