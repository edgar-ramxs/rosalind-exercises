# GenBank Introduction
# https://rosalind.info/problems/gbk/

# INFO:
# https://biopython.org/
# https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec200

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    GENUS, DATE_START, DATE_END = file.read().strip().split()

from Bio import Entrez

Entrez.email = "holacomoestas@gmail.com"
handle = Entrez.esearch(
    db="nucleotide",
    term=f'{GENUS}[Organism] AND("{DATE_START}"[Publication Date]: "{DATE_END}"[Publication Date])',
)
record = Entrez.read(handle)
output = f'{record["Count"]}'

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
