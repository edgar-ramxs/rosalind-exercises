# Square in a Graph
# https://rosalind.info/problems/sq/


## INFO:
# https://rosalind.info/glossary/algo-simple-graph/
# https://www.geeksforgeeks.org/cycles-of-length-n-in-an-undirected-and-connected-graph/


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_sq.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTICES, EDGES = [], [], []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            k_graph = len(GRAPHS) - 1
            # undirected graph in square matrix
            GRAPHS[k_graph][node1 - 1][node2 - 1] = 1
            GRAPHS[k_graph][node2 - 1][node1 - 1] = 1
        else:
            V, E = map(int, file.readline().strip().split(" "))
            matrix = [[0] * V for _ in range(V)]
            GRAPHS.append(matrix)
            VERTICES.append(V)
            EDGES.append(E)


def count_cycles(graph: list, length_cycle: int):

    def DFS(graph: list, marked: list, n: int, vert: int, start: int, count: int):
        marked[vert] = True
        if n == 0:
            marked[vert] = False
            if graph[vert][start] == 1:
                count = count + 1
                return count
            else:
                return count
        for i in range(len(graph)):
            if marked[i] == False and graph[vert][i] == 1:
                count = DFS(graph, marked, n - 1, i, start, count)
        marked[vert] = False
        return count

    count = 0
    marked = [False] * len(graph)
    for i in range(len(graph) - (length_cycle - 1)):
        count = DFS(graph, marked, length_cycle - 1, i, i, count)
        marked[i] = True
    if (count / 2) > 0:
        return 1
    return -1


OUTPUT = ""
for graph in GRAPHS:
    OUTPUT += f"{count_cycles(graph, 4)} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
