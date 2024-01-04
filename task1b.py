inputFile = open('input1b_3.txt', 'r')
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
else:
    indegree=[0]*(n_vertices+1)
    queue=[]
    sorted_list=[]
# The vertex which has incoming edge, it will be incremented by 1
    for i in dict1:
        for j in dict1[i]:
            indegree[j]+=1
# The vertex which has no in-degree will be appended to the queue first
    for j in range(1,len(indegree)):
        if indegree[j]==0:
            queue.append(j)
    while queue:
        current_vertex=queue.pop(0)
        sorted_list.append(current_vertex)
        if current_vertex in dict1:
            for adjacency_vertex in dict1[current_vertex]:
                indegree[adjacency_vertex] -= 1
                if indegree[adjacency_vertex] == 0:
                    queue.append(adjacency_vertex)
    result=' '.join(map(str,sorted_list))
outputFile=open('output1b_3.txt', 'w')
outputFile.writelines(result)
inputFile.close()
outputFile.close()