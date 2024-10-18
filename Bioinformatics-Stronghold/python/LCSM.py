# Finding a Shared Motif
# https://rosalind.info/problems/lcsm/

# INFO:
# https://rosalind.info/glossary/motif/
# https://en.wikipedia.org/wiki/Longest_common_substring#Suffix_tree

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

from Bio import SeqIO

DNA_COLLECTION = [
    str(aux.seq) for aux in SeqIO.parse(f"./inputs/{args.file_name}", "fasta")
]


def finding_shared_motif1(dna_collection: list = DNA_COLLECTION):

    def search_substrings(short_string):
        o = []
        k = len(short_string)

        while k > 0:
            x = set()
            for i in range(0, len(short_string) - k + 1):
                x.add(short_string[i : i + k])
            o += x
            k -= 1

        return o

    def if_substr_in_all(substr, l):
        for i in l:
            if substr not in i:
                return False
        return True

    records = sorted(dna_collection, key=lambda i: len(i))
    short_string = records[0]
    other_strings = records[1:]
    substrings = search_substrings(short_string)

    for substr in substrings:
        if if_substr_in_all(substr, other_strings):
            return substr

    return ""


def finding_shared_motif2(array: list = DNA_COLLECTION):

    def is_common_substring(array, substring):
        return all(substring in string for string in array)

    shortest_str = min(array, key=len)
    array.remove(shortest_str)
    length = len(shortest_str)
    start, end, motif = 0, length, ""

    while start <= end:
        step = (start + end) // 2
        for i in range(0, length - step + 1):
            substring = shortest_str[i : i + step]
            if is_common_substring(array, substring):
                start = step + 1
                motif = substring
                break
        else:
            end = step - 1
    return motif


OUTPUT = finding_shared_motif1()
# OUTPUT = finding_shared_motif2()

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(OUTPUT))
