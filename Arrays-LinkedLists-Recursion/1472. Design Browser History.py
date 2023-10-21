class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.head = self.curr
        self.tail = self.curr
        self.size = 1
        

    def visit(self, url: str) -> None:
        new = Node(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = new
        self.tail = new
        self.size += 1
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev is None:  
                break
            self.curr = self.curr.prev
        return self.curr.val
            
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next is None:  
                break
            self.curr = self.curr.next
        return self.curr.val

        