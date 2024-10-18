# Read Quality Distribution
# https://rosalind.info/problems/phre/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

with open(f"./inputs/{args.file_name}", "r") as file:
    threshold = int(file.readline().strip())
    count = 0
    records = SeqIO.parse(file, "fastq")

    for record_fastq in records:
        quality = record_fastq.letter_annotations["phred_quality"]
        average = sum(quality) / len(quality)
        if average < threshold:
            count += 1


OUTPUT = str(count)
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)