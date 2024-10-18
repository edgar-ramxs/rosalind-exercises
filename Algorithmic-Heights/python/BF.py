# Bellman-Ford Algorithm
# https://rosalind.info/problems/bf/


## INFO:
# https://rosalind.info/glossary/algo-bellman-ford-algorithm/
# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_bf.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}
    
    for line in file.readlines():
        node1, node2, weight = map(int, line.strip().split())
        GRAPH[node1].append((node2, weight))


def bellman_ford1(graph: dict, origin: int = 1) -> str:
    distances = {node: float("inf") for node in graph}
    distances[origin] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] != float("inf") and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] != float("inf") and distances[node] + weight < distances[neighbor]:
                distances[neighbor] = "x"

    output = ""
    for node, distance in distances.items():
        if distance == float("inf"):
            output += f"x "
        else:
            output += f"{distance} "

    return output


def bellman_ford2(graph: dict, origin: int = 1) -> str:
    distances = {node: float("inf") for node in graph}
    distances[origin] = 0

    for _ in range(len(graph) - 1):
        for node_origin, adjacents in graph.items():
            for node_destiny, weight in adjacents:
                new_distance = distances[node_origin] + weight
                if new_distance < distances[node_destiny]:
                    distances[node_destiny] = new_distance

    for node_origin, adjacents in graph.items():
        for node_destiny, weight in adjacents:
            new_distance = distances[node_origin] + weight
            if new_distance < distances[node_destiny]:
                return {node: "x" for node in graph}

    output = ""
    for node, distance in distances.items():
        if distance == float("inf"):
            output += f"x "
        else:
            output += f"{distance} "

    return output


OUTPUT = bellman_ford1(GRAPH)
# OUTPUT = bellman_ford2(GRAPH)


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
