# Finding Genes with ORFs
# https://rosalind.info/problems/orfr/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio.Seq import Seq
from Bio import BiopythonWarning
from warnings import filterwarnings

filterwarnings("ignore", category=BiopythonWarning)

with open(f"./inputs/{args.file_name}", "r") as file:
    DNA = file.readline().strip()


def finding_genes_with_orfs(dna_string: str = DNA) -> str:
    sequence = Seq(dna_string)
    reverse_sequence = sequence.reverse_complement()

    orf, orf_len = "", 0

    for string in [sequence, reverse_sequence]:
        for index in range(3):
            translates = str(string[index:].translate(stop_symbol="*")).split("*")
            orfs = [orf[orf.find("M") :] for orf in translates if "M" in orf]
            if orfs:
                borf = max(orfs, key=lambda orf: len(orf))
                borfl = len(borf)
                if borfl > orf_len:
                    orf = borf
                    orf_len = borfl

    return orf


OUTPUT = finding_genes_with_orfs()

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)