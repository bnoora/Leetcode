class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: 
                            l += 1
                        while l < r and nums[r] == nums[r-1]: 
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:
                        r -= 1
        return res
        