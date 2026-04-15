# Node class represents each element in the binary tree
class Node:
    def __init__(self, value):
        self.value = value      # store value of node
        self.left = None        # left child (initially empty)
        self.right = None       # right child (initially empty)


# BinaryTree class to manage the tree
class BinaryTree:
    def __init__(self):
        self.root = None        # initially tree is empty
        print("Created new Binary Tree")
        print("Root:", self.root)

    # Function to calculate height (max depth of tree)
    def height(self, node):
        if node is None:
            return 0            # if no node, height is 0
        # height = 1 + max height of left and right subtree
        return 1 + max(self.height(node.left), self.height(node.right))

    # Function to count total number of nodes
    def size(self, node):
        if node is None:
            return 0
        # count current node + left subtree + right subtree
        return 1 + self.size(node.left) + self.size(node.right)

    # Function to count leaf nodes (nodes with no children)
    def count_leaves(self, node):
        if node is None:
            return 0
        # if both children are None, it's a leaf node
        if node.left is None and node.right is None:
            return 1
        # otherwise check left and right subtree
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # Function to check if tree is a full binary tree
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        # leaf node → valid full tree
        if node.left is None and node.right is None:
            return True
        # node must have both children
        if node.left and node.right:
            return (self.is_full_binary_tree(node.left) and
                    self.is_full_binary_tree(node.right))
        # if only one child → not full
        return False

    # Function to check if tree is a complete binary tree
    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        queue = []              # use queue for level order traversal
        queue.append(self.root)
        flag = False            # becomes True when a missing child is found

        while queue:
            temp = queue.pop(0)

            # check left child
            if temp.left:
                if flag:        # if we already saw a missing child before
                    return False
                queue.append(temp.left)
            else:
                flag = True     # missing child found

            # check right child
            if temp.right:
                if flag:
                    return False
                queue.append(temp.right)
            else:
                flag = True

        return True


# --------- MAIN PROGRAM ---------

# Create Binary Tree object
bt = BinaryTree()

# Manually creating a perfect binary tree (7 nodes)
# Structure:
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# Display results
print("\nTree Height:", bt.height(bt.root))          # expected 3
print("Total Nodes:", bt.size(bt.root))              # expected 7
print("Leaf Nodes Count:", bt.count_leaves(bt.root)) # expected 4
print("Is Full Binary Tree:", bt.is_full_binary_tree(bt.root))  # True
print("Is Complete Binary Tree:", bt.is_complete_binary_tree()) # True