# Introduction to the Bioinformatics Armory
# https://rosalind.info/problems/ini/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    OUTPUT = ""
    DNA = file.readline().strip()

dna_string = sorted(set(DNA))
for nucleotides in dna_string:
    OUTPUT += f"{DNA.count(nucleotides)} "


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
