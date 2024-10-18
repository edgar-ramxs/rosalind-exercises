# Breadth-First Search
# https://rosalind.info/problems/bfs/


## INFO:
# https://rosalind.info/glossary/algo-breadth-first-search/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_bfs.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = list(map(int, file.readline().strip().split()))
    GRAPH = {node + 1: [] for node in range(V)}

    for line in file:
        node1, node2 = list(map(int, line.rsplit()))
        GRAPH[node1].append(node2)


def breadth_first_search(graph: dict = GRAPH, vertexes: int = V, start: int = 1) -> list:
    distances = [-1] * (vertexes + 1)
    distances[start] = 0
    queue = [start]

    while queue:
        current_vertex = queue.pop(0)
        for neighbor in graph.get(current_vertex, []):
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

    return distances[1:]


DISTANCES = breadth_first_search()
OUTPUT = " ".join(map(str, DISTANCES))


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
