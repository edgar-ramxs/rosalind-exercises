# Topological Sorting
# https://rosalind.info/problems/ts/


## INFO:
#


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_ts.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}
    NODES = set()

    for line in file.readlines():
        node1, node2 = map(int, line.rstrip().split(" "))
        GRAPH[node1].append(node2)
        NODES.add(node1)
        NODES.add(node2)


def Topological_Sorting(g: dict = GRAPH, n: set = NODES) -> str:
    graph, nodes = g.copy(), n.copy()
    output = ""

    def indegree_node(thegraph, indgree=0):
        out_nodes = []
        for node1 in thegraph.keys():
            counter = 0
            for node2 in thegraph:
                if node1 in thegraph[node2]:
                    counter += 1
            if counter == indgree:
                out_nodes.append(node1)
        return out_nodes

    while indegree_node(graph) != []:
        output += " ".join(map(str, indegree_node(graph))) + " "
        for one in indegree_node(graph):
            graph.pop(one)
            nodes.remove(one)

    return output


OUTPUT = Topological_Sorting()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
