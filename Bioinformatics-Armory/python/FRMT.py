# Data Formats
# https://rosalind.info/problems/frmt/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    INPUT = file.readline().strip().split()

from Bio import Entrez, SeqIO

Entrez.email = "holacomoestas@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=[", ".join(INPUT)], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

the_shortest_fasta = min(records, key=lambda x: len(x.seq)).format("fasta")

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(the_shortest_fasta)
