class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for i in range(len(pair)):
            if not stack:
                stack.append(pair[i])
                continue
            zero_time = (target - stack[-1][0]) / stack[-1][1]
            curr_time = (target - pair[i][0]) / pair[i][1]
            if stack and zero_time < curr_time:
                stack.append(pair[i])
            

        return len(stack)


print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

