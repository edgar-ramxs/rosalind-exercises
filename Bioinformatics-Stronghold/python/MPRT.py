# https://rosalind.info/problems/mprt/
# Finding a Protein Motif

from argparse import ArgumentParser


parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    PROTEINS = file.read().strip().split()
    protein_to_fetch = list(protein_id.split("_")[0][:6] for protein_id in PROTEINS)


import re
from Bio import SeqIO
from io import StringIO
from urllib.request import urlopen


def obtener_Seq(protein_id: str):
    url = f"https://rest.uniprot.org/uniprotkb/{protein_id}.fasta"
    try:
        with urlopen(url) as handle:
            fasta_data = handle.read().decode("utf-8")
            record = SeqIO.read(StringIO(fasta_data), "fasta")
        return record
    except Exception as e:
        print("Error al leer el archivo FASTA desde la URL:", e)
        return None


motif_regex = "N[^P][ST][^P]"


def motif_matches_in_string(s: str, pattern: str = motif_regex, base: int = 1) -> list:
    starting_positions = list()
    matches = re.finditer(r"(?=({0})).".format(pattern), s)
    for match in matches:
        starting_positions.append(match.start() + base)
    return starting_positions


output = ""
for index in range(len(PROTEINS)):

    protein_id = protein_to_fetch[index]
    protein_fasta = obtener_Seq(protein_id)
    positions = motif_matches_in_string(str(protein_fasta.seq))

    if positions:
        output += f"{PROTEINS[index]}\n"
        output += " ".join([str(pos) for pos in positions]) + "\n"

# print(output)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
