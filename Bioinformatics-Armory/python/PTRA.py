# Protein Translation
# https://rosalind.info/problems/ptra/

# INFO:
# TABLES => https://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    DNA = file.readline().strip()
    PROTEIN = file.readline().strip()

# print(DNA)
# print(PROTEIN)

from Bio.Data import CodonTable
from Bio.Seq import translate
from Bio import BiopythonWarning
from warnings import filterwarnings

filterwarnings("ignore", category=BiopythonWarning)


def protein_translation(dna: str = DNA, protein: str = PROTEIN):
    indices = []
    for table_id in CodonTable.ambiguous_generic_by_id.keys():
        try:
            translated_protein = translate(dna, table=table_id, to_stop=True)
            # print(translated_protein)
            if protein == translated_protein:
                indices.append(table_id)
        except:
            continue
    return indices


indices = protein_translation()

if indices:
    print(f"Lista de indices: {indices}")
    OUTPUT = str(indices[0])
    with open(f"./outputs/output_{args.file_name}", "w") as output_file:
        output_file.write(OUTPUT)
else:
    print(f"Lista de indices vacia: {indices}")
