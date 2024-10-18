# Double-Degree Array
# https://rosalind.info/problems/ddeg/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ddeg.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

def counting_degree_vertex(node1: int, node2: int, dictionary: dict):
    if not node1 in dictionary:
        dictionary[node1] = [1, node2]
    else:
        dictionary[node1][0] += 1
        dictionary[node1].append(node2)


with open(PATH_INPUT, "r") as file:
    V, E = list(map(int, file.readline().strip().split()))
    DEGREE_NEIGHBORS = {}

    for line in file:
        node1, node2 = map(int, line.rstrip().split())
        counting_degree_vertex(node1, node2, DEGREE_NEIGHBORS)
        counting_degree_vertex(node2, node1, DEGREE_NEIGHBORS)


OUTPUT = ""
for node in range(1, V + 1):
    count = 0
    if not node in DEGREE_NEIGHBORS:
        OUTPUT += f"0 "
    else:
        for neighbors in DEGREE_NEIGHBORS[node][1:]:
            count += DEGREE_NEIGHBORS[neighbors][0]
        OUTPUT += f"{count} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
