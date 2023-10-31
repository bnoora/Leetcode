class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        max_length = 0
        set1 = set()

        while right < len(s):
            if s[right] not in set1:
                set1.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                set1.remove(s[left])
                left += 1

        return max_length