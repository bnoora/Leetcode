class Solution:
    def removeDuplicates(self, nums) -> int:

        left = 1

        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i-1]
                left += 1
        
        print(nums)
        return left

                
# test
nums = [1,2]
print(Solution().removeDuplicates(nums))
                
                