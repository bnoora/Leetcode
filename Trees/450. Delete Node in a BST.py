class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        if root == None:
            return None
        
        if root.val == key:
            if root.left == None and root.right == None:
                return None
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                temp = root.right
                while temp.left != None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        
def buildTree(values):
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def printTree(root):
    if not root:
        return []
    output = []
    queue = [root]
    while any(queue):
        current = queue.pop(0)
        if current:
            output.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            output.append(None)
    while output[-1] is None:
        output.pop()
    return output

tree = buildTree([5,2,6,1,4,None,7,None,None,3])
print(printTree(tree))
new_tree = Solution().deleteNode(tree, 4)
print(printTree(new_tree))
        