# Fibonacci Numbers
# https://rosalind.info/problems/fibo/

## INFO:
# http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf      (pag 12 - pag 14)


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_fibo.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    N = int(file.readline().strip())


# DYNAMIC PROGRAMMING
def fibonacci(n: int = N):
    fibo_dp = [0, 1]
    if n <= 1:
        return n
    for _ in range(n + 1):
        fibo_dp.append(fibo_dp[-1] + fibo_dp[-2])
    return fibo_dp[n]


# Explanation in Rosalind
def Fibo(n: int = N):
    
    def sqrt(n: int):
        return n**0.5

    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2**n * sqrt(5)))


OUTPUT = str(fibonacci())
# OUTPUT = str(Fibo())


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
