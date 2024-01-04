inputFile = open('input1a_3.txt', 'r')
f_line = list(map(int, inputFile.readline().split(' ')))
n_vertices, m_edges = f_line[0], f_line[1]
dict1 = {}
# Representing the directed graph with Adjacency List
for i in range(m_edges):
    graph = list(map(int, inputFile.readline().split(' ')))
    ver1, ver2 = graph
    try:
        dict1[ver1].append(ver2)
    except KeyError:
        dict1[ver1] = [ver2]
# DFS Traversal. For finding a cycle in a graph DFS should be used.
visited = [False] * (n_vertices + 1)
stack = [False] * (n_vertices + 1)
check = False
def cycle_finding(dict1, current_vertex):
    global check
    visited[current_vertex] = True
    stack[current_vertex] = True
    if current_vertex in dict1:
        for adjacency_vertex in dict1[current_vertex]:
            if stack[adjacency_vertex]:
                check = True
            if not visited[adjacency_vertex]:
                cycle_finding(dict1, adjacency_vertex)
    stack[current_vertex] = False
    return check
# If check is True then the map contains a cycle. Otherwise it doesn't contain any cycle.
for current_vertex in range(1, n_vertices+1):
    if not visited[current_vertex]:
        if cycle_finding(dict1, current_vertex):    # If check==True
            result='IMPOSSIBLE'     # If there is any cycle found
            break
# If there is no cycle found then this block of code goes for topological sort
# Create a stack and a visited array to keep track of the order of nodes and visited nodes respectively.
# Perform a DFS on the graph, starting from every unvisited node.
# During DFS, mark the node as visited, call DFS recursively on all its adjacent nodes,
# and after visiting all adjacent nodes, push the node to the stack.
else:
    visited2 = [False]*(n_vertices+1)
    stack2 = []
    def topological_sort(current_vertex):
        visited2[current_vertex] = True
        if current_vertex in dict1:
            for adjacency_vertex in dict1[current_vertex]:
                if not visited2[adjacency_vertex]:
                    topological_sort(adjacency_vertex)
        stack2.append(current_vertex)
    for current_vertex in range(1, n_vertices+1):
        if not visited2[current_vertex]:
            topological_sort(current_vertex)
    result=' '.join(map(str,stack2[::-1]))
outputFile=open('output1a_3.txt', 'w')
outputFile.writelines(result)
inputFile.close()
outputFile.close()