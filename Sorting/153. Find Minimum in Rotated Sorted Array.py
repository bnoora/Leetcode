class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
        

class Solution2:
    def findMin(self, nums: [int]) -> int:
        return sorted(nums)[0]

class Solution3:
    def findMin(self, nums: [int]) -> int:
        return min(nums)
    
class Solution4:
    def findMin(self, nums: [int]) -> int:
        min1 = float('inf')
        for num in nums:
            min1 = min(min1, num)
        return min1