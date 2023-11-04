class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        stack = []
        max_area = 0
        

        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area


print(Solution().largestRectangleArea([2,1,5,6,2,3]))
