class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        if temperatures == []:
            return []
        if len(temperatures) == 1:
            return [0]
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))
        return result

