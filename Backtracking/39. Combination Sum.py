class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        ret = []


        def combinationSum_h(i, comb):
            tot = sum(comb)
            print(comb)
            if tot == target:
                ret.append(comb.copy())
                return
            
            if i >= len(candidates) or tot > target:
                return
            
            # choose same element
            comb.append(candidates[i])
            combinationSum_h(i, comb)
            comb.pop()

            # choose next element
            if i + 1 < len(candidates):
                comb.append(candidates[i+1])
                combinationSum_h(i+1, comb)
                comb.pop()
        combinationSum_h(0, [])
        return ret