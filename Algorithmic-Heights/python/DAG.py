# Testing Acyclicity
# https://rosalind.info/problems/dag/

## INFO:
# https://www.kaggle.com/code/bemc22/ordenamiento-topologico


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_dag.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS = []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            # Directed Graph
            graph[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)


def testing_acyclicity(graphs: list = GRAPHS) -> str:

    def dfs(graph: dict, vertice: int, visited: list, process: list) -> bool:
        if visited[vertice]:
            if vertice in process:
                return True
            return False
        visited[vertice] = True
        process.append(vertice)
        for neighbor in graph[vertice]:
            if dfs(graph, neighbor, visited, process):
                return True
        process.remove(vertice)
        return False

    def is_cyclical(graph: dict, vertices: int) -> int:
        visited = [False] * (vertices + 1)
        for node in range(1, vertices + 1):
            if dfs(graph, node, visited, []):
                return -1
        return 1

    output = ""
    for graph in graphs:
        result = is_cyclical(graph, len(graph))
        output += f"{result} "
    return output


OUTPUT = testing_acyclicity()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
