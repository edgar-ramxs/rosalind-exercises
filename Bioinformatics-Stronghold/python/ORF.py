# Open Reading Frames
# https://rosalind.info/problems/orf/

# INFO:
# https://www.biostars.org/p/9543290/
# https://biopython.org/DIST/docs/tutorial/Tutorial.html

import re
from argparse import ArgumentParser
from Bio import SeqIO

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


DNA_FASTA = SeqIO.read(f"./inputs/{args.file_name}", "fasta")
RNA_CODONS = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "STOP",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "STOP",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "STOP",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def open_reading_frames1(
    dna_string: object = DNA_FASTA.seq, rna_codons: dict = RNA_CODONS
):

    def translation(rna: str):
        protein = ""
        for i in range(0, len(rna), 3):
            stop = False
            if i + 3 < len(rna):
                peptide = rna_codons[rna[i : i + 3]]
                if peptide == "STOP":
                    stop = True
                    break
                protein += peptide
        if stop == True:
            return protein

    rna1 = dna_string.transcribe()
    rna2 = dna_string.reverse_complement().transcribe()

    start_coden = "AUG"
    ORFS = []

    for i in range(3):
        rna = rna1[i:]
        for j in range(0, len(rna), 3):
            if rna[j : j + 3] == start_coden:
                result = translation(rna[j:])
                if result:
                    ORFS.append(result)

    for i in range(3):
        rna = rna2[i:]
        for j in range(0, len(rna), 3):
            if rna[j : j + 3] == start_coden:
                result = translation(rna[j:])
                if result:
                    ORFS.append(result)

    return "\n".join(set(ORFS))


def open_reading_frames2(dna_string: object = DNA_FASTA.seq):
    sr = dna_string.reverse_complement()
    ss = [dna_string, dna_string[1:-2], dna_string[2:-1], sr, sr[1:-2], sr[2:-1]]
    prots = set()

    for s in ss:
        prots.update(
            (
                mo.groups()[0][:-1]
                for mo in re.finditer(r"(?=(M\w*\*))", str(s.translate()))
                if mo
            )
        )

    output = "\n".join(prots)

    return output


def open_reading_frames3(
    dna_string: object = DNA_FASTA.seq, rna_codons: dict = RNA_CODONS
):
    rna_seq = str(dna_string.transcribe())
    reverse_comp = str(dna_string.reverse_complement().transcribe())

    pattern = re.compile(r"(?=(AUG(?:...)*?)(?=UAA|UAG|UGA))")
    frags = []
    for s in re.findall(pattern, rna_seq):
        frags.append(s)
    for s in re.findall(pattern, reverse_comp):
        frags.append(s)

    output = set()

    for sequence in frags:
        split_codons = []
        prot_seq = []
        for i in range(0, len(sequence), 3):
            codon = sequence[i : i + 3]
            split_codons.append(codon)
        for s in split_codons:
            prot_seq.append(rna_codons[s])
        for i in prot_seq:
            output.add("".join(prot_seq))
            break

    return "\n".join(output)


OUTPUT = open_reading_frames1()
# OUTPUT = open_reading_frames2()
# OUTPUT = open_reading_frames3()


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
