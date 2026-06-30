class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                left = stack[-1][0] if stack else -1
                width = i - left - 1
                area = height * width
                max_area = max(max_area, area)


            stack.append((i,h))

        while stack:
            index, height = stack.pop()
            left = stack[-1][0] if stack else -1
            width = len(heights) - left - 1
            area = height * width
            max_area = max(max_area, area)


        return max_area
        