class Solution:
    def pathSum(self, root, sum):
        self.count = 0
        preDict = {0: 1}

        def dfs(p, sum, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - sum, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, sum, pathSum, preDict)
                dfs(p.right, sum, pathSum, preDict)
                preDict[pathSum] -= 1

        dfs(root, sum, 0, preDict)
        return self.count

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
Solution().pathSum(root, 8)