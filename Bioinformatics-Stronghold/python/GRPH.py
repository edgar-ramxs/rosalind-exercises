# Overlap Graphs
# https://rosalind.info/problems/grph/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

DNA_COLLECTION_FASTA = list(SeqIO.parse(f"./inputs/{args.file_name}", "fasta"))


def Overlap_Graphs(dna_collections: list = DNA_COLLECTION_FASTA, k: int = 3) -> str:
    output = ""
    for dna1 in dna_collections:
        dna_string1 = str(dna1.seq)

        for dna2 in dna_collections:
            dna_string2 = str(dna2.seq)

            if dna_string1 == dna_string2:
                continue

            if dna_string1[-k:] == dna_string2[:k]:
                output += f"{dna1.id} {dna2.id}\n"

    return output


OUTPUT = Overlap_Graphs()
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
