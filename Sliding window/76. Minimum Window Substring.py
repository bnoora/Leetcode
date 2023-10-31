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
