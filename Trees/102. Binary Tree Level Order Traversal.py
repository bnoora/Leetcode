from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        if not root:
            return []
        ret = []

        q = deque()
        q.append(root)
        while len(q) > 0: 
            rets = []
            for i in range(len(q)):
                node = q.popleft()
                rets.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(rets)

        return ret
                

