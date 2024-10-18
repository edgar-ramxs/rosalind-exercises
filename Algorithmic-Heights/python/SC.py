# Semi-Connected Graph
# https://rosalind.info/problems/sc/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_sc.txt"
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

###############################################################################
import numpy as np


def BFS(start_vertice, vertice, graph):
    quene, order = [], []
    distance = {i + 1: 0 for i in range(vertice)}
    quene.append(start_vertice)
    order.append(start_vertice)
    while quene:
        v = quene.pop(0)
        for n in graph[v]:
            if n not in order:
                distance[n] = distance[v] + 1
                order.append(n)
                quene.append(n)
    for k in distance.keys():
        if k not in order:
            distance[k] = -1
    return order, distance


def ifSemiConnectedGraph(graph, vertice):
    results = 1
    matrix = np.array([[0] * vertice for v in range(vertice)])
    for v in range(vertice):
        matrix[v][v] += 1

    for v in range(vertice):
        order, distance = BFS(v + 1, vertice, graph)
        for k in distance.keys():
            if distance[k] != -1:
                matrix[v][k - 1] += 1
                matrix[k - 1][v] += 1
            else:
                matrix[v][k - 1] -= 1
                matrix[k - 1][v] -= 1
        matrix_flatten = matrix.flatten()
        if -2 in matrix_flatten:
            return -1
    return 1

OUTPUT = ""
for graph in GRAPHS:
    OUTPUT += f"{ifSemiConnectedGraph(graph, len(graph))} "

with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)