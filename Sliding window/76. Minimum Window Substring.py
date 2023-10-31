class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict = {}
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        left = 0
        right = 0
        min_length = float('inf')
        count = {}
        start = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            while self.match(count, tdict):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                count[s[left]] = count.get(s[left]) - 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            right += 1
        return "" if min_length == float('inf') else s[start: start + min_length]

    
    def match(self, count, tdict):
        for k, v in tdict.items():
            if k not in count or count[k] < v:
                return False
        return True
