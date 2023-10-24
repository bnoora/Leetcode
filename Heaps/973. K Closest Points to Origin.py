import math
import heapq

class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        res = []
        pointsheap = []
        for i in points:
            pointsheap.append((math.sqrt(i[0]**2 + i[1]**2), i))
        heapq.heapify(pointsheap)
        for i in range(k):
            i, val = heapq.heappop(pointsheap)
            res.append(val)
        return res



