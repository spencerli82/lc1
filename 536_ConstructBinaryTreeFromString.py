class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        ix = S.find('(')
        if ix < 0:
            return TreeNode(int(S)) if S else None

        bal = 0
        for jx, u in enumerate(S):
            if u == '(': bal += 1
            if u == ')': bal -= 1
            if jx > ix and bal == 0:
                break

        root = TreeNode(int(S[:ix]))
        root.left = self.str2tree(S[ix + 1:jx])
        root.right = self.str2tree(S[jx + 2:-1])
        return root

s = "4(2(3)(1))(6(5))"
print Solution().str2tree(s)