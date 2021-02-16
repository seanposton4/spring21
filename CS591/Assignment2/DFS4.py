#DFS networkx
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_nodes_from([6, 7, 8, 9])

G.add_edge(5, 8)
G.add_edge(5, 4)
G.add_edge(5, 7)
G.add_edge(8, 2)
G.add_edge(4, 3)
G.add_edge(4, 1)
G.add_edge(7, 6)
G.add_edge(6, 9)

nx.draw(G, with_labels = True, font_weight = 'bold')

#output = list(nx.dfs_preorder_nodes(G, source = 5))

plt.show()