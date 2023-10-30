class Solution:
    def trap(self, height: [int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        ans = 0

        while l < r:
            if l_max < r_max:
                l += 1
                if l_max > height[l]:
                    ans += l_max - height[l]
                else:
                    l_max = height[l]
            else:
                r -= 1
                if r_max > height[r]:
                    ans += r_max - height[r]
                else:
                    r_max = height[r]

        return ans