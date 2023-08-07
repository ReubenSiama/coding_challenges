# Find minimum depth
binary_tree = [3,9,20,None,None,15,7]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print("Height of the tree is ", maxDepth(root))
