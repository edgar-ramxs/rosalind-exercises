# General Sink
# https://rosalind.info/problems/gs/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_gs.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS = []

    for line in file:
        if line.strip():
            node1, node2 = map(int, line.strip().split(" "))
            graph[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)


def find_reachable_vertex(graph: dict):
    for vertex in graph:
        reachable = set()
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            reachable.add(current_vertex)

            for neighbor in graph[current_vertex]:
                if neighbor not in reachable:
                    stack.append(neighbor)

        if len(reachable) == len(graph):
            return vertex

    return -1


OUTPUT = ""
for graph in GRAPHS:
    result = find_reachable_vertex(graph)
    OUTPUT += f"{result} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
