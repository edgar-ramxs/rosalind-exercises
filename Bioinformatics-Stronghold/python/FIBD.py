# Mortal Fibonacci Rabbits
# https://rosalind.info/problems/fibd/

# INFO:
# https://stackoverflow.com/questions/17310051/fibonacci-rabbits-dying-after-arbitrary-of-months
# https://noobest.medium.com/rosalind-mortal-fibonacci-rabbits-8c8e83c359db
# https://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html
# https://medium.com/du-phan/dynamic-programming-and-mortal-fibonacci-rabbits-4570a2c0dca6

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N, M = map(int, file.readline().strip().split())
    # print(N, M)


def mortal_fibonacci_rabbits_1(n: int = N, m: int = M):
    living = [1, 1]
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    return living[-1]


def mortal_fibonacci_rabbits_2(n: int = N, m: int = M):
    population = [[0] * m for _ in range(n + 1)]
    population[1][0] = 1

    for month in range(2, len(population)):
        for age in range(0, len(population[0])):
            if age == 0:
                population[month][age] = sum(population[month - 1][1:])
            else:
                population[month][age] = population[month - 1][age - 1]

    return sum(population[n])


def mortal_fibonacci_rabbits_3(n: int = N, m: int = M):
    generations = [
        1,
        1,
    ]
    count = 2
    while count < n:
        if count < m:
            generations.append(
                generations[-2] + generations[-1]
            )  # recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
        elif count == m or count == m + 1:
            # print("in base cases for newborns (1st+2nd gen. deaths)")
            # Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            generations.append(
                (generations[-2] + generations[-1]) - 1
            )  # Fn = Fn-2 + Fn-1 - 1
        else:
            generations.append(
                (generations[-2] + generations[-1]) - (generations[-(m + 1)])
            )  # Our recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
        count += 1
    return generations[-1]


# print(mortal_fibonacci_rabbits_1(N, M))
# print(mortal_fibonacci_rabbits_2(N, M))
# print(mortal_fibonacci_rabbits_3(N, M))
OUTPUT = str(mortal_fibonacci_rabbits_3(N, M))

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
