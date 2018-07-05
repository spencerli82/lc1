class Solution(object):
    def __init__(self):
        self.lSum = 0
    def convertBST(self, root):
        if not root:
            return None
        self.convertBST(root.right)
        self.lSum += root.val
        root.val = self.lSum
        self.convertBST(root.left)
        return root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
Solution().convertBST(root)