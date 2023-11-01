import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1_dict = collections.defaultdict(int)
        s2_dict = collections.defaultdict(int)

        for c in range(len(s1)): 
            s1_dict[s1[c]] += 1
            s2_dict[s2[c]] += 1
        i = 0
        
        for c in range(len(s1)-1, len(s2)):
            if s1_dict == s2_dict: return True
            s2_dict[s2[i]] -= 1
            if s2_dict[s2[i]] == 0: del s2_dict[s2[i]]
            if (c+1) < len(s2): s2_dict[s2[c+1]] += 1
            i += 1
            print(s2_dict)
        return False
        

        