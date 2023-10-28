class Solution:
    def climbStairs(self, n: int) -> int:
        last, last2 = 1, 1

        for i in range(n-1):
            last, last2 = last + last2, last
        return last
    
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [1,2]
        for i in range(2,n):
            new = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = new
        return dp[1]