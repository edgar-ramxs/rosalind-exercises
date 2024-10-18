# Transcribing DNA into RNA
# https://rosalind.info/problems/rna/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    RNA = file.read().strip().replace("T", "U")

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(RNA)
