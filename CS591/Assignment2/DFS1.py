#DFS non recursive
def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return 'Invalid Input'
    path = []
    stack = [source]
    while (len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            continue    
        for neighbor in graph[s]:
            stack.append(neighbor)
    return ' '.join(path)

def main():
    graph = {
        'A': ['D', 'C', 'B'],
        'B': ['E'],
        'C': ['F', 'G'], #The example has G, F but that seems wrong.
        'D': ['H'],
        'E': ['I'],
        'F': ['J']
    }

    path = dfs_non_recursive(graph, 'A')
    print(path)
main()