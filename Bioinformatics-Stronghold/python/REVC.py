# Complementing a Strand of DNA
# https://rosalind.info/problems/revc/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    DNA = file.readline().strip()


def reverse_complement(dna: str = DNA):
    dna_complement = ""
    for c in dna[::-1]:
        dna_complement += {"A": "T", "C": "G", "G": "C", "T": "A"}[c]
    return dna_complement


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(reverse_complement())
