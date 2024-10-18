# Negative Weight Cycle
# https://rosalind.info/problems/nwc/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_nwc.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTICES, EDGES = [], [], []

    for line in file:
        data = list(map(int, line.rstrip().split(" ")))
        if len(data) == 3:
            node1, node2, weight = data
            graph[node1].append((node2, weight))
        elif len(data) == 2:
            V, E = data
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)


def bellman_ford(graph: dict) -> int:
    for source in graph:
        distances = {vertex: float("inf") for vertex in graph}
        distances[source] = 0
        changed = True
        for _ in range(len(graph) - 1):
            if not changed:
                break
            changed = False
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        changed = True
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    return 1
    return -1


OUTPUT = ""
for graph in GRAPHS:
    is_negative_weight_cycle = bellman_ford(graph)
    OUTPUT += f"{is_negative_weight_cycle} "


with open(PATH_OUTPUT , "w") as output_file:
    output_file.write(OUTPUT)
