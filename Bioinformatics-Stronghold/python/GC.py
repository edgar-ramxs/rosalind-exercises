# Computing GC Content
# https://rosalind.info/problems/gc/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

dna_in_fasta = list(SeqIO.parse(f"./inputs/{args.file_name}", "fasta"))


def Computing_GC_Content(dna_records=dna_in_fasta) -> str:
    temp = -1
    output = ""
    for record in dna_records:

        # Old Version
        # total_character = len(record.seq)
        # gc_count = record.seq.count("G") + record.seq.count("C")
        # gc_percentage = (gc_count / total_character) * 100

        # Version of Bio.SeqUtils
        gc_percentage = gc_fraction(record.seq) * 100

        if gc_percentage > temp:
            output = f"{record.id}\n{gc_percentage}"
            temp = gc_percentage
    return output


OUTPUT = Computing_GC_Content()


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
