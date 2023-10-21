# Instrtion sort
class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j+1] < nums[j]:
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp
                j -= 1
        return nums
    

# merge sort
class Solution2:
    def sortArray(self, nums: [int]) -> [int]:
        return self.merge_sort(nums, 0, len(nums)-1)
        
    def merge_sort(self, nums: [int], start: int, end: int) -> [int]:
        if (-start + end + 1 <= 1):
            return nums
        mid = (start + end) // 2
        self.merge_sort(nums, start, mid)
        self.merge_sort(nums, mid+1, end)

        self.merger(nums, start, mid, end)
        return nums
    
    def merger(self, nums, start, mid, end):
        left = nums[start: mid+1]
        right = nums[mid+1: end+1]

        i = 0
        j = 0
        k = start

        # if left[i] < right[j]: assign num at k pointer to nums[i] and vice versa
        while i < len(left) and j < len(right):
            if (left[i] < right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
        return nums

# quick sort
class Solution3:
    def sortArray(self, nums: [int]) -> [int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[-1]
        replacor = 0
        iterator = 0

        while iterator < len(nums)-1:
            if nums[iterator] < pivot:
                temp = nums[replacor]
                nums[replacor] = nums[iterator]
                nums[iterator] = temp
                replacor += 1
            iterator += 1
        nums[-1], nums[replacor] = nums[replacor], pivot
        left = self.sortArray(nums[:replacor])
        right = self.sortArray(nums[replacor+1:])
        return left + [pivot] + right

class Solution4:
    def sortArray(self, nums: [int]) -> [int]:
        pass


        




