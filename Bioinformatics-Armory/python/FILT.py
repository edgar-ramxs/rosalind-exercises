# Read Filtration by Quality
# https://rosalind.info/problems/filt/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

with open(f"./inputs/{args.file_name}", "r") as file:
    threshold, percentage = map(int, file.readline().strip().split())
    # print(threshold)
    # print(percentage)
    count = 0
    records = SeqIO.parse(file, "fastq")

    for record_fastq in records:

        quality = record_fastq.letter_annotations["phred_quality"]
        quality_th = [qth for qth in quality if qth >= threshold]

        if ( len(quality_th) / len(quality) ) * 100 >= percentage:
            count += 1


OUTPUT = str(count)
# print(OUTPUT)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)