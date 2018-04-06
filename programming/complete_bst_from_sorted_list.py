import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(traverse_tree(self))

def num_nodes(level):
    n = 0
    for i in range(level+1):
        n += pow(2, i)

    return n

def traverse_tree(root):
    """
    traverse in-order for validation
    """
    tree = []
    if root.left:
        tree.extend(traverse_tree(root.left))

    tree.append(root.val)

    if root.right:
        tree.extend(traverse_tree(root.right))

    return tree

def complete_bst(data):
    if not data:
        return None

    if len(data) == 1:
        return Node(data[0])

    print('Data: {}'.format(data))

    n = len(data)
    print('Total nodes: {}'.format(n))

    height = int(math.log(n, 2))
    print('Height: {}'.format(height))

    leaf_nodes = n - num_nodes(height-1)
    print('leaf nodes: {}'.format(leaf_nodes))

    if leaf_nodes != pow(2, height):
        # how many leaf nodes in the list are to the left of root
        leaf_nodes_on_left = min(leaf_nodes, pow(2, height)/2)
        root_idx = (num_nodes(height-1)/2) + leaf_nodes_on_left
    else:
        # complete + perfect bst
        leaf_nodes_on_left = 0
        root_idx = (num_nodes(height)/2) + leaf_nodes_on_left

    print('leaf nodes on left of root: {}'.format(leaf_nodes_on_left))

    print('Root: {}, index: {}'.format(data[root_idx], root_idx))

    root = Node(data[root_idx])

    root.left = complete_bst(data[:root_idx])
    root.right = complete_bst(data[root_idx+1:])

    return root

root = complete_bst(range(9))

print(root)