
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#recursive
class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        arr = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        return arr
        

#iterative
class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        arr = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            arr.append(current.val)
            current = current.right
        return arr

        
