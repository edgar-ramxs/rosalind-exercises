# Shortest Cycle Through a Given Edge
# https://rosalind.info/problems/cte/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_cte.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################


with open(PATH_INPUT, "r") as file:
    K = int(file.readline().strip())
    GRAPHS, edge = [], {}

    for line in file:
        if len(line.rstrip().split(" ")) == 2:
            nodenum = int(line.rstrip().split(" ")[0])
            if edge != {}:
                GRAPHS.append((edge, firstedge))
            edge = {}
        elif len(line.rstrip().split(" ")) == 3:
            start, end, length = line.rstrip().split(" ")
            if edge == {}:
                firstedge = (start, end)
            edge[(start, end)] = int(length)
    GRAPHS.append((edge, firstedge))


def dfs(graph: dict, node: int) -> set:
    visited = set()
    search(graph, node, visited)
    return visited


def search(graph: dict, node: int, visited: set) -> None:
    visited.add(node)
    for theedge in graph.keys():
        if theedge[0] == node:
            if theedge[1] not in visited:
                search(graph, theedge[1], visited)


def shortest_cycle_through_a_given_edge(graph: dict, specialedge: tuple) -> int:
    node_start, node_end = specialedge[0], specialedge[1]
    downnodes = dfs(graph, specialedge[1])
    d = {}

    if node_start not in downnodes:
        return -1

    for node in downnodes:
        d[node] = graph[(node_end, node)] if (node_end, node) in graph else float("inf")

    for m in range(len(downnodes)):
        for edge in graph.keys():
            if edge[0] in downnodes and edge[1] in downnodes:
                if d[edge[1]] > d[edge[0]] + graph[edge]:
                    d[edge[1]] = d[edge[0]] + graph[edge]

    return d[node_start] + graph[specialedge]


OUTPUT = ""
for graph_data in GRAPHS:
    OUTPUT += f"{shortest_cycle_through_a_given_edge(*graph_data)} "


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
