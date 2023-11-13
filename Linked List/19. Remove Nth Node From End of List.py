
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        counterNode = ListNode(0, head)
        first = head
        second = counterNode

        while n:
            first = first.next
            n -= 1

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return counterNode.next
        