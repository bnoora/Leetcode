class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        curr = self.head
        currn = self.head.next
        new.next = self.head.next
        new.prev = self.head
        currn.prev = new
        curr.next = new
        self.size += 1


        
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        curr = self.tail
        currp = self.tail.prev
        new.next = curr
        new.prev = currp
        currp.next = new
        curr.prev = new
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        curr = self.head
        for _ in range(index + 1):  # Adjusted the range to index + 1
            curr = curr.next
        new = Node(val)
        new.next = curr
        new.prev = curr.prev
        curr.prev.next = new
        curr.prev = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index + 1):  # Adjusted to get to the actual node to delete
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1


    def printList(self) -> None:
        curr = self.head.next  # Start from the first node after the dummy head
        while curr != self.tail:  # Stop before the dummy tail
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")  # To signify the end of the linked list




myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.printList()
myLinkedList.addAtTail(3)
myLinkedList.printList()
myLinkedList.addAtIndex(1, 2)    
myLinkedList.printList()
myLinkedList.get(1)            
myLinkedList.deleteAtIndex(1)    
myLinkedList.get(1)       