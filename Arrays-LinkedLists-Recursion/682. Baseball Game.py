class Solution:
    def calPoints(self, operations: [str]) -> int:
        if not operations:
            return 0
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
        