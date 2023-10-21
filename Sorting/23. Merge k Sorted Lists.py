class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            lists = merged

def mergeTwoLists(list1, list2):
    templist = ListNode(0)
    tmplist = templist

    while list1 and list2:
        if list1.val < list2.val:
            tmplist.next = list1
            list1 = list1.next
        else:
            tmplist.next = list2
            list2 = list2.next
        tmplist = tmplist.next
    
    while list1:
        tmplist.next = list1
    while list2:
        tmplist.next = list2
    
    return templist.next
        