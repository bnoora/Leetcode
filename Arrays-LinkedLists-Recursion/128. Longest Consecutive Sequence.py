class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        bucket = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in bucket:
                curr_len = 1
                while num + 1 in bucket:
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len