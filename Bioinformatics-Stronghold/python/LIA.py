# Independent Alleles
# https://rosalind.info/problems/lia/

# INFO:
# https://es.wikipedia.org/wiki/Distribuci%C3%B3n_binomial
# https://en.wikipedia.org/wiki/Mendelian_inheritance#Law_of_Independent_Assortment
# https://aliquote.org/post/rosalind-independent-alleles/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K, N = map(int, file.readline().strip().split())
    # K -> number of generations
    # N -> least number of the population with genotype Aa Bb we are looking for

from math import factorial


def independent_alleles1(k: int = K, n: int = N, decimals: int = 3) -> float:
    population = 2**K
    probability = 0
    for i in range(n, population + 1):
        prob = (
            (factorial(population) / (factorial(i) * factorial(population - i)))
            * (0.25**i)
            * (0.75 ** (population - i))
        )
        probability += prob

    return round(probability, decimals)


def independent_alleles2(k: int = K, n: int = N, decimals: int = 3) -> float:
    def nCr(n, r):
        return factorial(n) / factorial(r) / factorial(n - r)

    prob_AaBb = 4 / 16.0
    prob = []
    total = 2**k
    for r in range(N, (total + 1)):
        prob.append(nCr(total, r) * (prob_AaBb**r) * ((1 - prob_AaBb) ** (total - r)))

    return round(sum(prob), decimals)


from scipy.special import binom


def independent_alleles3(k: int = K, n: int = N, decimals: int = 3) -> float:
    def p(n, k):
        return binom(2**k, n) * 0.25**n * 0.75 ** (2**k - n)

    output = 1 - sum(p(n, k) for n in range(N))
    return round(output, decimals)


OUTPUT = independent_alleles1()
# OUTPUT = independent_alleles2()
# OUTPUT = independent_alleles3()


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(OUTPUT))
