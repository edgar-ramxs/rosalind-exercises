# BIP
# https://rosalind.info/problems/bip/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_bip.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTICES, EDGES = [], [], []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            # Undirected Graph
            graph[node1].append(node2)
            graph[node2].append(node1)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)
            VERTICES.append(V)
            EDGES.append(E)


def testing_bipartiteness1(graphs: list = GRAPHS, k: int = K) -> str:

    def bip_test(grafo: dict, vertice: int, visitados: list, color: list) -> bool:
        for i in grafo[vertice]:
            if not visitados[i]:
                visitados[i] = True
                color[i] = not color[vertice]
                if not bip_test(grafo, i, visitados, color):
                    return False
            else:
                if color[vertice] == color[i]:
                    return False
        return True

    output = ""
    for i in range(k):
        graph, num_vertices = graphs[i], VERTICES[i]
        visited = [False for v in range(num_vertices + 1)]
        color = [False for v in range(num_vertices + 1)]
        visited[1] = True

        if bip_test(graph, 1, visited, color):
            output += f"{1} "
        else:
            output += f"{-1} "
    
    return output


def testing_bipartiteness2(graphs: list = GRAPHS, k: int = K) -> str:

    def bip_test(graph: dict) -> int:
        colors = {}
        for vertex in graph:
            if vertex not in colors:
                colors[vertex] = 0
                queue = [vertex]
                front = 0
                while front < len(queue):
                    current_vertex = queue[front]
                    current_color = colors[current_vertex]
                    front += 1
                    for neighbor in graph[current_vertex]:
                        if neighbor not in colors:
                            colors[neighbor] = 1 - current_color
                            queue.append(neighbor)
                        elif colors[neighbor] == current_color:
                            return -1
        return 1

    output = ""
    for graph in graphs:
        output += f"{bip_test(graph)} "

    return output


# OUTPUT = testing_bipartiteness1()
OUTPUT = testing_bipartiteness2()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
