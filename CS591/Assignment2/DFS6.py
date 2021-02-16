#Connected components DFS
import networkx as nx
import matplotlib.pyplot as plt

def dfs_traversal(graph, start, visited, path):
        if start in visited:
            return visited, path
        visited.append(start)
        path.append(start)
        for node in graph.neighbors(start):
            visited, path = dfs_traversal(graph, node, visited, path)
        return visited, path

def find_connected_components(graph):
    visited = []
    connected_components = []
    for node in graph.nodes:
        if node not in visited:
            cc = []
            visited, cc = dfs_traversal(graph, node, visited, cc)
            connected_components.append(cc)
    return connected_components

def main():
    graph = nx.Graph()
    graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    graph.add_edges_from([('A', 'B'), ('B', 'E'), ('A', 'E')])
    graph.add_edges_from([('C', 'D'), ('D', 'H'), ('H', 'F'), ('F', 'C')])
    graph.add_edge('G', 'I')

    nx.draw(graph, with_labels =  True, font_weight='bold')
    plt.show()

    connected_components = find_connected_components(graph)
    print(f'Total number of connected components = {len(connected_components)}')

    for cc in connected_components:
        print(cc)

main()
