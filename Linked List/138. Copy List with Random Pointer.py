
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: [Node]) -> [Node]:
        if not head: return None

        copyDict = {}
        curr = head

        # create copies of the nodes and store in copyDict
        while curr:
            copyDict[curr] = Node(curr.val, None, None)
            curr = curr.next

        # reset curr to head for the second pass
        curr = head

        # assign next and random pointers
        while curr:
            if curr.next:
                copyDict[curr].next = copyDict[curr.next]
            if curr.random:
                copyDict[curr].random = copyDict[curr.random]
            curr = curr.next

        return copyDict[head]





