# mem efficiant
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict = {}
        scount = 0
        tcount = 0
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
            tcount += 1
        left = 0
        right = 0
        min_length = float('inf')
        count = {}
        start = 0


        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while count == tdict:
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

# time efficiant
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        tdict = {}
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        required = len(tdict)
        matched = 0
        window_counts = {}
        left, right = 0, 0
        min_len = float('inf')
        min_window_start = 0

        while right < len(s):
            window_counts[s[right]] = window_counts.get(s[right], 0) + 1

            if s[right] in tdict and window_counts[s[right]] == tdict[s[right]]:
                matched += 1

            while left <= right and matched == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_start = left
                
                window_counts[s[left]] -= 1

                # Move the left pointer
                if s[left] in tdict and window_counts[s[left]] < tdict[s[left]]:
                    matched -= 1
                
                left += 1
            
            right += 1

        return "" if min_len == float('inf') else s[min_window_start: min_window_start + min_len]
