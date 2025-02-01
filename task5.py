import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#999999"  # Початковий колір (сірий)
        self.id = str(uuid.uuid4())  # Унікальний ID для графа


def build_tree():
    """Створює тестове дерево."""
    root = Node(10)
    root.left = Node(15)
    root.right = Node(20)
    root.left.left = Node(30)
    root.left.right = Node(40)
    root.right.left = Node(50)
    root.right.right = Node(60)
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Рекурсивно додає вузли та ребра в граф."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_tree(tree_root):
    """Візуалізує дерево."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def generate_colors(n):
    """Генерує n кольорів від темного до світлого."""
    base_color = (18 / 255, 150 / 255, 240 / 255)  # RGB #1296F0
    colors = [
        mcolors.to_hex(
            (
                base_color[0] + i / n * (1 - base_color[0]),
                base_color[1] + i / n * (1 - base_color[1]),
                base_color[2] + i / n * (1 - base_color[2]),
            )
        )
        for i in range(n)
    ]
    return colors


def bfs_traversal(root):
    """Обхід у ширину (BFS) з візуалізацією."""
    if not root:
        return

    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    visualize_traversal(root, order, "Обхід у ширину (BFS)")


def dfs_traversal(root):
    """Обхід у глибину (DFS) з візуалізацією."""
    if not root:
        return

    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    visualize_traversal(root, order, "Обхід у глибину (DFS)")


def visualize_traversal(root, order, title):
    """Відображає кожен крок обходу з унікальним кольором вузла."""
    colors = generate_colors(len(order))

    for i, node in enumerate(order):
        node.color = colors[i]  # Призначення кольору
        plt.clf()
        print(f"Відвідуємо вузол: {node.val}")
        draw_tree(root)
        time.sleep(1)  # Пауза для анімації


# === Запуск програми ===
tree_root = build_tree()
print("Виберіть тип обходу:")
print("1 - Обхід у глибину (DFS)")
print("2 - Обхід у ширину (BFS)")
choice = input("Введіть 1 або 2: ")

if choice == "1":
    dfs_traversal(tree_root)
elif choice == "2":
    bfs_traversal(tree_root)
else:
    print("Невірний вибір!")
