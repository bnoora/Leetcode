class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]