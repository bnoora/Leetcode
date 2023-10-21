class Solution:
    def climbStairs(self, n: int) -> int:
        last, last2 = 1, 1

        for i in range(n-1):
            last, last2 = last + last2, last
        return last