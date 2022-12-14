import networkx as nx
import matplotlib.pyplot as plt

L=nx.Graph()
L.add_node('M')
L.add_node('A2')
L.add_node('A4')
L.add_node('B')
L.add_node('A1')
L.add_node('A3')
L.add_node('A5')
L.add_node('LY1')
L.add_node('LY2')
L.add_node('LY3')
L.add_node('LY4')
L.add_node('LY5')
L.add_node('LY6')
L.add_node('LY7')
L.add_node('LY8')
L.add_node('LY9')
L.add_node('D4')
L.add_node('D3')
L.add_node('D2')

nx.draw(L, with_labels = True, node_size = 500)
plt.margins(0.05)
plt.show()