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
        root = node
        return root

    if node.value < root.value:
        root.left = insert(root.left, node)
        
    if node.value > root.value:
        root.right = insert(root.right, node)
        
    return root

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

# Populating a Tree
root = Node(50)
insert(root, Node(10))
insert(root, Node(2))
insert(root, Node(80))
insert(root, Node(15))
insert(root, Node(60))
insert(root, Node(90))

# Preorder traverals of a Tree
preorder(root)
print()

# Inorder traverals of a Tree
inorder(root)
