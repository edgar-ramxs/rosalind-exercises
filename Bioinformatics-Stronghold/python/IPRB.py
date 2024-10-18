# Mendel's First Law
# https://rosalind.info/problems/iprb/

# INFO:
# https://susannahgo.files.wordpress.com/2015/11/rosalind-iprb.pdf
# https://www.youtube.com/watch?v=8X7WNs6R2zQ&list=WL&index=1&t=478s


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    INPUT = list(map(int, file.read().strip().split()))
    # print(K, M, N)
    # [0] -> k -> homozygous dominant   ->  AA
    # [1] -> m -> heterozygous          ->  Aa
    # [2] -> n -> homozygous recessive  ->  aa

import numpy as np


def firts_law_medel(organisms: list = INPUT) -> float:
    population = sum(organisms)
    dominant_fraction, sum_props, probabilities = [], [], []

    AA = np.array([[0, 0]])
    Aa = np.array([[0, 1]])
    aa = np.array([[1, 1]])

    for i in range(3):
        for j in range(3):
            if i != j:
                probability = (organisms[i] / population) * (
                    organisms[j] / (population - 1)
                )
            else:
                probability = (organisms[i] / population) * (
                    (organisms[j] - 1) / (population - 1)
                )
            probabilities.append(probability)
    for i in [AA, Aa, aa]:
        for j in [AA, Aa, aa]:
            matrix = i.T * j
            fraction = np.sum(matrix == 0) / 4.0
            dominant_fraction.append(fraction)
    for i in range(0, 9):
        sum_props.append(dominant_fraction[i] * probabilities[i])
    return sum(sum_props)


def firts_law_medel_2(organisms: list = INPUT) -> float:
    def take_two(n):
        return n * (n - 1) // 2

    dominants, heteroz, recessives = organisms
    total_pairs = take_two(sum(organisms))

    dominant_pairs = (
        take_two(dominants)  # Dos homocigotos dominantes
        + 3 / 4 * take_two(heteroz)  # Dos heterocigotos
        + dominants * heteroz  # Un homocigoto dominante y un heterocigoto
        + dominants * recessives  # Un homocigoto dominante y un homocigoto recesivo
        + 1 / 2 * heteroz * recessives  # Un heterocigoto y un homocigoto recesivo
    )

    probability = dominant_pairs / total_pairs

    return probability


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(firts_law_medel()))
