# 2-Satisfiability
# https://rosalind.info/problems/2sat/


## INFO:
# https://en.wikipedia.org/wiki/2-satisfiability
# https://codeforces.com/blog/entry/16205
# https://cp-algorithms.com/graph/2SAT.html
# https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/
# https://imada.sdu.dk/u/jbj/DM19/2SAT.pdf
# https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# https://www.wikiwand.com/en/2-satisfiability


## PASS FILE NAME VIA COMMAND LINE ARGUMENTS
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Input data file name")
# parser.add_argument("-file", "--file_name", type=str, help="Input data document name (file.txt)")
# FILE_NAME = parser.parse_args().__dict__["file_name"]


## CONSTANTS
FILE_NAME = "rosalind_2sat.txt"
PATH_INPUT = f"./inputs/{FILE_NAME}"
PATH_OUTPUT = f"./outputs/output_{FILE_NAME}"

################################################################################################

def dfs1_iterative(start_vertex, used, order, graph):
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if used[v]:
            continue
        used[v] = True
        order.append(v)
        for u in graph[v]:
            if not used[u]:
                stack.append(u)


def dfs2_iterative(start_vertex, cl, comp, graph_t):
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if comp[v] != -1:
            continue
        comp[v] = cl
        for u in graph_t[v]:
            if comp[u] == -1:
                stack.append(u)


def solve_2sat(n, graph, graph_t):
    output = ""
    order = []
    used = [False] * n
    for i in range(n):
        if not used[i]:
            dfs1_iterative(i, used, order, graph)

    comp = [-1] * n
    j = 0
    for i in range(n):
        v = order[n - i - 1]
        if comp[v] == -1:
            j += 1
            dfs2_iterative(v, j, comp, graph_t)

    assignment = [False] * (n // 2)
    for i in range(0, n, 2):
        if comp[i] == comp[i + 1]:
            output += f"{0}"
            return output
        assignment[i // 2] = comp[i] > comp[i + 1]

    output += f"{1} "
    for i in range(len(assignment)):
        if assignment[i]:
            output += f"{i + 1} "
        else:
            output += f"{-(i + 1)} "
    return output


################################################################################################

with open(PATH_INPUT, "r") as f:
    k = int(f.readline().strip())
    graphs, graphs_t, variables = [], [], []
    graph, graph_t = None, None

    for line in f:
        if line.strip():
            a, b = map(int, line.strip().split(" "))
            if a > 0 and b > 0:
                graph[2 * abs(a) - 1].append(2 * abs(b) - 2)
                graph[2 * abs(b) - 1].append(2 * abs(a) - 2)
                graph_t[2 * abs(b) - 2].append(2 * abs(a) - 1)
                graph_t[2 * abs(a) - 2].append(2 * abs(b) - 1)
            elif a < 0 and b > 0:
                graph[2 * abs(a) - 2].append(2 * abs(b) - 2)
                graph[2 * abs(b) - 1].append(2 * abs(a) - 1)
                graph_t[2 * abs(b) - 2].append(2 * abs(a) - 2)
                graph_t[2 * abs(a) - 1].append(2 * abs(b) - 1)
            elif a > 0 and b < 0:
                graph[2 * abs(a) - 1].append(2 * abs(b) - 1)
                graph[2 * abs(b) - 2].append(2 * abs(a) - 2)
                graph_t[2 * abs(b) - 1].append(2 * abs(a) - 1)
                graph_t[2 * abs(a) - 2].append(2 * abs(b) - 2)
            else:
                graph[2 * abs(a) - 2].append(2 * abs(b) - 1)
                graph[2 * abs(b) - 2].append(2 * abs(a) - 1)
                graph_t[2 * abs(b) - 1].append(2 * abs(a) - 2)
                graph_t[2 * abs(a) - 1].append(2 * abs(b) - 2)
        else:
            variable, _ = map(int, f.readline().strip().split(" "))
            variables.append(variable)
            graph = [[] for _ in range(2 * variable)]
            graphs.append(graph)
            graph_t = [[] for _ in range(2 * variable)]
            graphs_t.append(graph_t)

output = ""
for i in range(k):
    graph = graphs[i]
    graph_t = graphs_t[i]
    variable = variables[i]
    output += solve_2sat(variable * 2, graph, graph_t)
    output += "\n"

with open(PATH_OUTPUT, "w") as output_file:
    output_file.write(output)
