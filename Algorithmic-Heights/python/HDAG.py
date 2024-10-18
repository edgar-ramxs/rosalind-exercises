# Hamiltonian Path in DAG
# https://rosalind.info/problems/hdag


## INFO:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tournament.hamiltonian_path.html


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_hdag.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTEXES, EDGES = [], [], []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            graph[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)
            VERTEXES.append(V)
            EDGES.append(E)


def hamiltonian_path(G: list = GRAPHS, V: list = VERTEXES, k: int = K) -> str:

    def topologicalsortUtil(v: int, visited: list, path: list) -> None:
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                topologicalsortUtil(i, visited, path)
        path.insert(0, v)

    def topologicalsort(graph: dict, vertice: int) -> list:
        visited = [False] * (vertice + 1)
        path = []
        for v in range(1, vertice + 1):
            if visited[v] == False:
                topologicalsortUtil(v, visited, path)
        return path

    def check_consecutive(path: list, graph: dict) -> bool:
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]]:
                return False
        return True

    # Hamiltonian Path in DAG => OUTPUT
    output = ""
    for n in range(k):
        graph = G[n]
        vertice = V[n]
        path = topologicalsort(graph, vertice)
        if check_consecutive(path, graph):
            output += f"{1} {' '.join(map(str, path))}\n"
        else:
            output += f"{-1}\n"

    return output


OUTPUT = hamiltonian_path()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
