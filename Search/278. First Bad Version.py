class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        prev = True
        previ = 0
        while low <= high:
            mid = (low + high) // 2
            guess = isBadVersion(mid) 
            if guess == True:
                prev = guess
                previ = mid
                high = mid - 1
            else:
                low = mid + 1 
        return previ
    
def isBadVersion(n):
    pass