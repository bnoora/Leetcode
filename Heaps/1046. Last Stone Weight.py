import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesheap = MaxHeap()
        for i in stones:
            stonesheap.push(i)
        
        while stonesheap.size() > 1:
            a = stonesheap.pop()
            b = stonesheap.pop()
            if a != b:
                stonesheap.push(a-b)
            if stonesheap.size() == 0:
                return 0
        return stonesheap.peek()

        

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def size(self):
        return len(self.heap)
