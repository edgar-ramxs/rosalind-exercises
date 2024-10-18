# Counting DNA Nucleotides
# https://rosalind.info/problems/dna/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    DNA = file.read().rstrip()


def counting_dna(dna: str = DNA) -> str:
    output = ""
    for aux in ["A", "C", "G", "T"]:
        output += f"{dna.count(aux)} "
    return output


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(counting_dna(DNA))
