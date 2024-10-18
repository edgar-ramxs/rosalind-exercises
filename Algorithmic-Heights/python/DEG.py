# Degree Array
# https://rosalind.info/problems/deg/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_deg.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

def counting_degree_vertex(node: int, dictionary: dict):
    if not node in dictionary:
        dictionary[node] = 1
    else:
        dictionary[node] += 1


with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split(" "))
    DEGREE_VERTEXS = {}

    for line in file:
        node1, node2 = map(int, line.strip().split(" "))
        counting_degree_vertex(node1)
        counting_degree_vertex(node2)


VERTEXS = sorted(DEGREE_VERTEXS.items())
OUTPUT = ""
for node, degree in VERTEXS:
    OUTPUT += f"{degree} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
