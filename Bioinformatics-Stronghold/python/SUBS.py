# Finding a Motif in DNA
# https://rosalind.info/problems/subs/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    S, T = file.read().strip().split()


def finding_motif_in_dna(s: str = S, t: str = T) -> str:
    ls, lt = len(s), len(t)
    locations = ""
    for i in range(ls):
        word = None
        if i + lt > ls:
            word = s[i:]
        else:
            word = s[i : i + lt]
        # Motif
        if word == t:
            locations += f"{i+1} "
    return locations


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(finding_motif_in_dna())
