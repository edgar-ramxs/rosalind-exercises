# Connected Components
# https://rosalind.info/problems/cc/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_cc.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = list(map(int, file.readline().strip().split()))
    GRAPH = {node + 1: [] for node in range(V)}
    for line in file:
        node1, node2 = map(int, line.strip().split())
        # undirected graph
        GRAPH[node1].append(node2)
        GRAPH[node2].append(node1)


def connected_components1(graph: dict = GRAPH) -> int:
    
    def dfs(vertex: int, visited: set) -> None:
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    components = 0
    for vertex in graph:
        if vertex not in visited:
            components += 1
            dfs(vertex, visited)
    return components


def connected_components2(graph: dict = GRAPH, nodes: int = V) -> int:
    
    def BFS(graph: dict, start: int, visited: list):
        stack = [start]
        visited[start] = True
        while stack:
            current_vertex = stack.pop()
            for neighbor in graph.get(current_vertex, []):
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

    visited = [False] * (nodes + 1)
    components = 0
    for vertex in range(1, nodes + 1):
        if not visited[vertex]:
            components += 1
            BFS(graph, vertex, visited)
    return components


OUTPUT = str(connected_components1())
# output = str(connected_components2())


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
