# Calculating Protein Mass
# https://rosalind.info/problems/prtm/

# INFO:
# https://rosalind.info/glossary/peptide-bond/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    PROTEIN = file.readline().strip()

MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333,
}


def protein_mass(protein: str, mass_table: dict = MONOISOTOPIC_MASS_TABLE, decimals: int = 3):
    count = 0
    for symbol in protein:
        if symbol in mass_table:
            count += mass_table[symbol]
    return round(count, decimals)

# BioPython
# from Bio.SeqUtils import molecular_weight
# answer = molecular_weight(PROTEIN, "protein", monoisotopic=True) - molecular_weight("", "protein", monoisotopic=True)
# print(round(answer, 3))

OUTPUT = protein_mass(PROTEIN)
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(OUTPUT))
