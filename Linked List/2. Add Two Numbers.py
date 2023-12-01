class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        new_list = ListNode()
        curr = new_list
        carryover = 0

        while l1 or l2:
            if l1:
                curr.val += l1.val
                l1 = l1.next
            if l2:
                curr.val += l2.val
                l2 = l2.next

            if curr.val >= 10:
                carryover = 1
                curr.val -= 10

            if l1 or l2 or carryover:
                curr.next = ListNode(carryover)
                curr = curr.next
                carryover = 0

        return new_list
        
        