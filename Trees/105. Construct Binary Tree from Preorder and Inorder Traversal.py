# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        midindx = inorder.index(preorder[0])
        print(midindx)  
        root.left = self.buildTree(preorder[1:midindx+1], inorder[:midindx])
        root.right = self.buildTree(preorder[midindx+1:], inorder[midindx+1:])


