class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        hashm = {}
        for i in nums:
            if i in hashm:
                return i
            else:
                hashm[i] = 1

