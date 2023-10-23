class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        ret = []

        subset = []
        def subset_h(i):
            if i >= len(nums):
                ret.append(subset.copy())
                return
            # choose
            subset.append(nums[i])
            subset_h(i+1)

            # not choose
            subset.pop()
            subset_h(i+1)
        subset_h(0)
        return ret


        



