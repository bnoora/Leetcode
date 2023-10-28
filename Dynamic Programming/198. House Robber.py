class Solution:
    def rob(self, nums: [int]) -> int:
        house1 , house2 = 0, 0
        for i in range(len(nums)):
            house1, house2 = house2, max(house1 + nums[i], house2)
        return house2
        
class Solution2:
    def rob(self, nums: [int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        memorize = [0]*len(nums)
        memorize[-1] = nums[-1]
        memorize[-2] = nums[-2]
        for i in range(len(nums)-3, -1, -1):
            memorize[i] = max(nums[i], nums[i] + max(memorize[i+2:]))
        return max(memorize[0], memorize[1])