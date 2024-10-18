# Base Quality Distribution
# https://rosalind.info/problems/bphr/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO
from functools import reduce

with open(f"./inputs/{args.file_name}", "r") as file:
    threshold = int(file.readline().strip())
    records = SeqIO.parse(file, "fastq")
    qualities = []
    count = None

    for record_fastq in records:
        quality = record_fastq.letter_annotations["phred_quality"]
        qualities.append(quality)

    if qualities:
        results = [sum(quality) for quality in zip(*qualities)]
        count = sum(1 for x in results if x / len(qualities) < threshold)


OUTPUT = str(count)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
