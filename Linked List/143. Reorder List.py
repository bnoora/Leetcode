class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node = slow
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half in-place
        curr = slow.next

        prev = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        # merge two sorted linked lists
        first, second = head, prev
        while second:
            tmp = first.next
            tmp2 = second.next
            first.next = second
            first = tmp
            second.next = tmp
            second = tmp2
        return head
    
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

node = Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
printList(node) # 1 5 2 4 3