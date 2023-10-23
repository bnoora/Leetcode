from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        if not root:
            return []
        ret = []

        q = deque()
        q.append(root)
        while q: 
            lvll = len(q)
            for i in range(lvll):
                node = q.popleft()
                if i == lvll - 1:
                    ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ret
    
tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
sol = Solution()
print(sol.rightSideView(tree))



        