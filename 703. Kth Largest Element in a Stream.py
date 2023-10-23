from collections import heapq

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.minHeap = nums 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if val < self.minHeap[1]:
            return self.minHeap[1]
        else:
            self.minHeap.append(val)
            heapq.heapify(self.minHeap)
            while len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            return self.minHeap[1]

        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)