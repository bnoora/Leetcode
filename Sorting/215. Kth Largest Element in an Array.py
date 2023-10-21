class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        pivot = nums[-1]
        itert = 0
        replace = 0

        while itert < len(nums) -1:
            if nums[itert] < pivot:
                temp = nums[itert]
                nums[itert] = nums[replace]
                nums[replace] = temp
                replace += 1
            itert += 1
        nums[-1], nums[replace] = nums[replace], pivot
        if replace == len(nums) - k:
            return nums[replace]
        elif replace < len(nums) - k:
            return self.findKthLargest(nums[replace+1:], k)
        else:
            return self.findKthLargest(nums[:replace], k - (len(nums) - replace))
 
