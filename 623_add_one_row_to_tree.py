import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def addOneRow(root, v, d):
    if d == 1:
        new_root = TreeNode(v)
        new_root.left = root
        return new_root
    queue = collections.deque()
    queue.append(root)
    depth = 1
    while queue:
        for _ in range(len(queue)):
            top = queue.popleft()
            if depth == d - 1:
                left, right = TreeNode(v), TreeNode(v)
                if top.left:
                    left.left = top.left
                if top.right:
                    right.right = top.right
                top.left, top.right = left, right
                continue
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        depth += 1
    return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
addOneRow(root, 1, 3)