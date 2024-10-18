# FASTQ format introduction
# https://rosalind.info/problems/tfsq/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

SeqIO.convert(
    f"./inputs/{args.file_name}", "fastq", f"./outputs/output_{args.file_name}", "fasta"
)
