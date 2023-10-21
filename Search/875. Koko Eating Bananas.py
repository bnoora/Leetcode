class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1

        return res
