# Strongly Connected Components
# https://rosalind.info/problems/scc/


## INFO:
# https://www.geeksforgeeks.org/strongly-connected-components/
# https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# https://gist.github.com/akueisara/120d8d5b4e1a663c606987b00e6c3c15
# https://es.wikipedia.org/wiki/Componente_fuertemente_conexo


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_scc.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

with open(PATH_INPUT, "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}
    EDGES = []

    for line in file.readlines():
        node1, node2 = map(int, line.strip().split())
        GRAPH[node1].append(node2)
        EDGES.append((node1, node2))


class Node:
    def __init__(self, value):
        self.value = value
        self.index = None
        self.lowlink = None
        self.on_stack = False
        self.neighbors = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].neighbors.append(self.nodes[v])

    def tarjan(self):
        index = 0
        stack = []
        scc = []
        scc_components = []

        def strong_connect(v):
            nonlocal index, stack, scc

            v.index = index
            v.lowlink = index
            index += 1
            stack.append(v)
            v.on_stack = True

            for neighbor in v.neighbors:
                if neighbor.index is None:
                    strong_connect(neighbor)
                    v.lowlink = min(v.lowlink, neighbor.lowlink)
                elif neighbor.on_stack:
                    v.lowlink = min(v.lowlink, neighbor.index)

            if v.lowlink == v.index:
                scc = []
                while stack:
                    w = stack.pop()
                    w.on_stack = False
                    scc.append(w.value)
                    if w == v:
                        break
                scc_components.append(scc)

        for node in self.nodes.values():
            if node.index is None:
                strong_connect(node)

        return scc_components


class GFG:
    def dfs(self, curr, des, adj, vis):
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False

    def isPath(self, src, des, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, des, adj, vis)

    def findSCC(self, n, a):
        ans = []
        is_scc = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])
        for i in range(1, n + 1):
            if not is_scc[i]:
                scc = [i]
                for j in range(i + 1, n + 1):
                    if (
                        not is_scc[j]
                        and self.isPath(i, j, adj)
                        and self.isPath(j, i, adj)
                    ):
                        is_scc[j] = 1
                        scc.append(j)
                ans.append(scc)
        return ans


# graph = Graph()
# for edge in EDGES:
#     graph.add_edge(edge[0], edge[1])
# scc_components = graph.tarjan()
# print(f"Strongly connected components: {len(scc_components)}")
# print()
obj = GFG()
ans = obj.findSCC(V, EDGES)
OUTPUT = f"{len(ans)}"
print(f"Strongly Connected Components are: {OUTPUT}")


with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(OUTPUT)
