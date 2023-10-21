class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1

        iterator = 0
        for i in range(0,len(counter)):
            while counter[i] > 0:
                nums[iterator] = i
                iterator += 1
                counter[i] -= 1

    
print(Solution().sortColors([2,0,1,1,2,0]))
