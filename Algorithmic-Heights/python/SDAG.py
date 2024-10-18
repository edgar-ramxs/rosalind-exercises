# Shortest Paths in DAG
# https://rosalind.info/problems/sdag/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_sdag.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: {} for node in range(V)}

    for line in file.readlines():
        node1, node2, weight = map(int, line.strip().split())
        GRAPH[node1][node2] = weight


def topologicalSort(v, visited, stack):
    visited[v] = True
    for u in GRAPH[v]:
        if visited[u] == False:
            topologicalSort(u, visited, stack)
    stack.append(v)


def shortestPath(graph, vertice, source):
    visited = [False] * (vertice + 1)
    stack = []
    for i in range(1, vertice + 1):
        if visited[i] == False:
            topologicalSort(i, visited, stack)
    distance = [float("inf")] * (vertice + 1)
    distance[source] = 0
    while stack:
        i = stack.pop()
        for u in graph[i]:
            if distance[i] != float("inf") and distance[u] > distance[i] + graph[i][u]:
                distance[u] = distance[i] + graph[i][u]
    return distance


distance = shortestPath(GRAPH, V, 1)
OUTPUT = ""
for i in GRAPH:
    if distance[i] == float("inf"):
        OUTPUT += f"x "
    else:
        OUTPUT += f"{distance[i]} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
