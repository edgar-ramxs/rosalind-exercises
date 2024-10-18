# Dijkstra's Algorithm
# https://rosalind.info/problems/dij/


## INFO:
# https://www6.uniovi.es/usr/cesar/Uned/EDA/Apuntes/TAD_apUM_07.pdf
# https://es.wikipedia.org/wiki/Grafo_ponderado
# https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra
# http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_dij.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}
    for line in file.readlines():
        node1, node2, weight = map(int, line.strip().split())
        GRAPH[node1].append((node2, weight))


def dijkstra1(graph: dict = GRAPH, node_origin: int = 1) -> str:
    distances = {node: float("inf") for node in graph}
    distances[node_origin] = 0
    visited = set()
    
    while visited != set(graph):
        current_node = min((node for node in distances if node not in visited), key=distances.get)
        visited.add(current_node)
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    output = ""
    for node, distance in distances.items():
        if distance == float("inf"):
            output += "-1 "
        else:
            output += f"{distance} "
    return output


def dijkstra2(graph: dict = GRAPH, node_origin: int = 1) -> str:
    distances = {node: float("inf") for node in graph}
    distances[node_origin] = 0
    visited = set()
    heap = [(0, node_origin)]

    while heap:
        min_dist = float("inf")
        min_vertice = None
        for dist, vertice in heap:
            if dist < min_dist and vertice not in visited:
                min_dist = dist
                min_vertice = vertice

        if min_vertice is None:
            break
        heap.remove((min_dist, min_vertice))
        visited.add(min_vertice)
        
        for neighbor, weight in graph[min_vertice]:
            if neighbor not in visited:
                new_distance = min_dist + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heap.append((new_distance, neighbor))

    output = ""
    for node, distance in distances.items():
        if distance == float("inf"):
            output += "-1 "
        else:
            output += f"{distance} "
    return output


# OUTPUT = dijkstra1()
OUTPUT = dijkstra2()


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
