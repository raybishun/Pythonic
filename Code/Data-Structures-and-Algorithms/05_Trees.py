# -----------------------------------------------------------------------------
# Trees (a non-linear data structure)
# -----------------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(root, node):
        if root is None:
            root = Node
            return root

        if node.value < root.value:
            root.left = insert(root.left, node)
        
        if node.value > root.value:
            root.right = insert(root.right, node)
        
        return root