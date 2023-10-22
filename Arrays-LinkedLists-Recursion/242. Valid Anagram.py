class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        for char in t:
            if char in dict:
                dict[char] -= 1
            else:
                return False
        for key in dict:
            if dict[key] != 0:
                return False
        return True
