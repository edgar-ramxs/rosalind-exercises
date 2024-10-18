# https://rosalind.info/problems/meme/
# New Motif Discovery

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

import re
from Bio import SeqIO

DATA = list(SeqIO.parse(f"./inputs/{args.file_name}", "fasta"))

for aux in DATA:
    print(str(aux.seq))
