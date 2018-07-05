class Solution(object):
    def pruneTree(self, root):
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val:
            return None
        return root



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
root.left.right.right = TreeNode(0)
print Solution().pruneTree(root)