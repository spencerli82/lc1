class Solution(object):
    def boundaryOfBinaryTree(self, root):
        res = []
        if not root: return res
        res.append(root.val)
        self.leftBoundary(root.left, res)
        self.leftLeaf(root.left, res)
        self.rightLeaf(root.right, res)
        self.rightBoundary(root.right, res)
        return res
    def leftBoundary(self, node, res):
        if not node or (not node.left and not node.right):
            return
        res.append(node.val)
        if node.left:
            self.leftBoundary(node.left, res)
        else:
            self.leftBoundary(node.right, res)
    def leftLeaf(self, node, res):
        if not node: return
        if not node.left and not node.right:
            res.append(node.val)
        self.leftLeaf(node.left, res)
        self.leftLeaf(node.right, res)
    def rightLeaf(self, node, res):
        if not node: return
        self.rightLeaf(node.left, res)
        self.rightLeaf(node.right, res)
        if not node.left and not node.right:
            res.append(node.val)
    def rightBoundary(self, node, res):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            self.rightBoundary(node.right, res)
        else:
            self.rightBoundary(node.left, res)
        res.append(node.val)

class Solution2(object):
    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary

class Solution3(object):
    def boundaryOfBinaryTree(self, root):
        if not root: return []

        left_bd_nodes = [root]
        cur = root.left
        while cur:
            left_bd_nodes.append(cur)
            cur = cur.left or cur.right

        right_bd_nodes = [root]
        cur = root.right
        while cur:
            right_bd_nodes.append(cur)
            cur = cur.right or cur.left

        leaf_nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                leaf_nodes.append(node)

        ans = []
        seen = set()

        def visit(node):
            if node not in seen:
                seen.add(node)
                ans.append(node.val)

        for node in left_bd_nodes: visit(node)
        for node in leaf_nodes: visit(node)
        for node in reversed(right_bd_nodes): visit(node)

        return ans

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)
Solution3().boundaryOfBinaryTree(root)