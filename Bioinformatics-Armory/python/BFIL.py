# Base Filtration by Quality
# https://rosalind.info/problems/bfil/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

with open(f"./inputs/{args.file_name}", "r") as file:
    QCV = int(file.readline().strip())
    records = SeqIO.parse(file, "fastq")
    output = ""
    for record_fastq in records:
        quality = record_fastq.letter_annotations["phred_quality"]
        start, end = 0, len(quality)

        while quality[start] < QCV:
            start += 1

        while quality[end - 1] < QCV:
            end -= 1

        output += record_fastq[start:end].format("fastq")


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
