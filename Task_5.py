import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import colorsys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#cccccc"
        self.id = str(uuid.uuid4())

def generate_gradient(n):
    colors = []
    for i in range(n):
        lightness = 0.2 + (0.7 * i / max(n - 1, 1))
        rgb = colorsys.hls_to_rgb(0.55, lightness, 0.7)

        hex_color = '#{:02x}{:02x}{:02x}'.format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )
        colors.append(hex_color)
    return colors

def dfs(root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)

    return visited

def bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return visited

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

    return graph

def draw_tree(root, order):
    colors = generate_gradient(len(order))

    for i, node in enumerate(order):
        node.color = colors[i]

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    node_colors = [data['color'] for _, data in tree.nodes(data=True)]
    labels = {n: d['label'] for n, d in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels,
            arrows=False,
            node_size=2500,
            node_color=node_colors)
    plt.show()

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("DFS visualization")
draw_tree(root, dfs(root))

print("BFS visualization")
draw_tree(root, bfs(root))