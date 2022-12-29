class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[(heights[0], 0)]
        i = 1
        max_area = heights[0]
        for bar in heights[1:]:
            if bar > stack[-1][0]:
                stack.append((bar,i))
            elif bar < stack[-1][0]:
                while len(stack)>0 and stack[-1][0] > bar:
                    c_h, c_p = stack.pop()
                    area = c_h*(i-c_p)
                    max_area = max(area, max_area)
                stack.append((bar,c_p))
            i = i+1
        while len(stack)>0:
            c_h, c_p = stack.pop()
            area = c_h*(i-c_p)
            max_area = max(area, max_area)
        return max_area   
