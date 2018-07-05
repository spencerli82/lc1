class Solution:
    def longestConsecutive(self, root):
        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            self.maxLen = max(self.maxLen , li + rd + 1, ld + ri + 1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0

        self.maxLen = 0
        dfs(root, root)
        return self.maxLen

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
Solution().longestConsecutive(root)