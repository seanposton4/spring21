#Recursive BFS Implementation
from collections import deque

class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]

        #add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

#Perform BFS recursively on the graph
def recursiveBFS(graph, q, discovered):
    if not q: return

    #dequeue front node and print it
    v = q.popleft()

    print(v, end=' ')

    #do for every edge `v -> `u
    for u in graph.adjList[v]:
        if not discovered[u]:
            #mark it as discovered and enqueue it 
            discovered[u] = True
            q.append(u)
    recursiveBFS(graph, q, discovered)

if __name__ == '__main__':
    #List of Graph edges:
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]

    N = 15
    #build a graph from edges
    graph = Graph(edges, N)

    discovered = [False] * N

    q = deque()

    for i in range(N):
        if not discovered[i]:
            discovered[i] = True

            q.append(i)

            recursiveBFS(graph, q, discovered)