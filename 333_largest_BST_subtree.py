class Solution(object):
    def largestBSTSubtree(self, root):
        def solve(root, maxval):
            if not root: return 0, float('inf'), -float('inf')
            left, minvl, maxvl = solve(root.left, maxval)
            right, minvr, maxvr = solve(root.right, maxval)
            if left == -1 or right == -1 or not maxvl < root.val < minvr:
                return -1, 0, 0
            maxval[0] = max(maxval[0], 1 + left + right)
            return 1 + left + right, min(root.val, minvl, minvr), max(root.val, maxvr, maxvl)

        maxval = [0]
        solve(root, maxval)
        return maxval[0]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
Solution().largestBSTSubtree(root)