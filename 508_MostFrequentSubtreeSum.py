class Solution(object):
    def findFrequentTreeSum(self, root):
        self.freq = dict()
        def dfs(node):
            if node is None:
                return 0
            total = dfs(node.left) + node.val + dfs(node.right)
            self.freq[total] = self.freq.get(total, 0) + 1
            return total
        dfs(root)
        inverse = [val for key, val in self.freq.items()]
        return [key for key, val in self.freq.items() if val == max(inverse)]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.left.right.right = TreeNode(3)
print Solution().findFrequentTreeSum(root)