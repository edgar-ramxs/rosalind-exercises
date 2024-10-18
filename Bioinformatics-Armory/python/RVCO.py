# Complementing a Strand of DNA
# https://rosalind.info/problems/rvco/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

records = SeqIO.parse(f"./inputs/{args.file_name}", "fasta")

count = 0
for req in records:
    dna = str(req.seq)
    reverse = str(req.seq.reverse_complement())
    if dna == reverse:
        count += 1
    

OUTPUT = str(count)
# print(OUTPUT)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)