class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1