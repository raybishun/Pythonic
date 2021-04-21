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

# Preorder traveral
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

# Inorder traveral
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

# Postorder traveral
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

# Binary Search Tree (BST)
def getMinimumValueNode(root):
    if root:
        while root.left is not None:
            root = root.left
        return root

# -----------------------------------------------------------------------------
# Consumer
# -----------------------------------------------------------------------------
# Populating a Tree
root = Node(50)
insert(root, Node(10))
insert(root, Node(2))
insert(root, Node(80))
insert(root, Node(15))
insert(root, Node(60))
insert(root, Node(90))

# Preorder traveral of a Tree
preorder(root)
print()

# Inorder traveral of a Tree
inorder(root)
print()

# Postorder traveral of a Tree
postorder(root)
print()

# Use a Binary Search Tree (BST) to return the minimum value node
print(getMinimumValueNode(root).value)
print()