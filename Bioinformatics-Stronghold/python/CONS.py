# Consensus and Profile
# https://rosalind.info/problems/cons/

# INFO:
# https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec167 (17.1.1 Creating a motif from instances)
# https://en.wikipedia.org/wiki/Consensus_sequence

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO, motifs

DNA_COLLECTION_FASTA = list(SeqIO.parse(f"./inputs/{args.file_name}", "fasta"))
data = motifs.create(DNA_COLLECTION_FASTA)

# print(data.counts)
output = f"{data.consensus}\n"

for linea in [
    aux.replace(".00", "").replace("   ", " ")
    for aux in str(data.counts).splitlines(keepends=True)[1:]
]:
    output += linea

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
