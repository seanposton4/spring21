#DFS Recursive 
def dfs_recursive(graph, source, path = []):
    if source not in path:
        path.append(source)

        if source not in graph:
            return path
        for neighbor in graph[source]:
            path = dfs_recursive(graph, neighbor, path)
    return path

def main():
    graph = {
        'A': ['D', 'C', 'B'],
        'B': ['E'],
        'C': ['F', 'G'], #The example has G, F but that seems wrong.
        'D': ['H'],
        'E': ['I'],
        'F': ['J']
    }

    path = dfs_recursive(graph, 'A')
    print(*path)
main()