inputFile = open('input3_2.txt', 'r')
f_line = list(map(int, inputFile.readline().split(' ')))
n_vertices, m_edges = f_line[0], f_line[1]
graph1, graph2 = {}, {}
for i in range(m_edges):
    ver1, ver2 = list(map(int, inputFile.readline().split(' ')))
# Representing the given graph with adjacency list
    try:
        graph1[ver1].append(ver2)
    except KeyError:
        graph1[ver1] = [ver2]
# Representing the transpose graph with adjacency list
    try:
        graph2[ver2].append(ver1)
    except KeyError:
        graph2[ver2] = [ver1]
# Kosaraju's Algorithm
# First traverse dfs same as for the topological sort on graph1
# Every time pop a vertex from the stack and traverse on graph2
stack = []
def find_scc(current_vertex, graph, visited, stack):
    visited[current_vertex] = True
    if current_vertex in graph:
        for adjacency_vertex in graph[current_vertex]:
            if not visited[adjacency_vertex]:
                find_scc(adjacency_vertex, graph, visited, stack)
    stack.append(current_vertex)
visited1 = [False] * (n_vertices + 1)
visited2 = [False] * (n_vertices + 1)
for current_vertex in range(1, n_vertices + 1):
    if not visited1[current_vertex]:
        find_scc(current_vertex, graph1, visited1, stack)
result = []
while stack:
    vertex = stack.pop()
    if not visited2[vertex]:
        component = []
        find_scc(vertex, graph2, visited2, component)
        result.append(component)
outputFile = open('output3_2.txt', 'w')
for i in result:
    outputFile.writelines(' '.join(map(str, i)) + '\n')
inputFile.close()
outputFile.close()
