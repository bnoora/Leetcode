
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: [Node]) -> [Node]:
        if not head: return None
        copyDict = []
        counter = 0

        # create copy of head   
        curr = head.next
        headCopy = Node(head.val, None, None)
        copyDict.append(headCopy)

        # create copy of rest of the nodes
        while curr:
            newNode = Node(curr.val, None, None)
            headCopy.next = newNode
            copyDict.append(newNode)
            curr = curr.next
            headCopy = headCopy.next
            counter += 1

        # assign random pointers
        while counter > 0:
            if head.random:
                copyDict[counter].random = copyDict[head.random.val]
            counter -= 1
            head = head.next

        
        return copyDict[0]
