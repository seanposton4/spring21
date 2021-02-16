#Iterative BFS
from collections import deque

class Graph:
    def __init__(self, edges, N):

        #A list of lists that represents an adjacency list
        self.adjList = [[] for _ in range(N)]

        #This adds edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

#Perform BFS on the graph with starting point 'v'
def BFS(graph, v, discovered):

    q = deque() #queue for BFS
    discovered[v] = True #source vertex marked discovered

    #This is a test for github
    #enqueue source vertex
    q.append(v)

    #loop till queue is empty
    while q:
        #dequeue front node and print it
        v = q.popleft()
        print(v, end=' ')

        #do for every edge `v -> `u
        for u in graph.adjList[v]:
            if not discovered[u]:
                #mark it as discovered and enqueue it
                discovered[u] = True
                q.append(u)

if __name__ == '__main__':
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        #vertexes 0, 13, and 14 are single nodes
    ]
    N = 15

    graph = Graph(edges, N)

    discovered = [False] * N
    
    for i in range(N):
        if not discovered[i]:
            BFS(graph, i, discovered)