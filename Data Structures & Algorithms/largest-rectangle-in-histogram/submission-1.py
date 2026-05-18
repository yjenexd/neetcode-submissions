class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i], i)) ##(7,0)
            elif heights[i] < stack[-1][0]:
                prev_index = 0
                while stack and heights[i] < stack[-1][0]:
                    prev_rect = stack.pop()
                    prev_height = prev_rect[0]
                    prev_index = prev_rect[1]
                    max_area = max(max_area, prev_height * (i - prev_index)) ## 7
                stack.append((heights[i], prev_index))
            elif heights[i] == stack[-1][0]:
                continue
            else:
                stack.append((heights[i], i))


        for height, index in stack:
                max_area = max(max_area, height * (len(heights) - index))

        return max_area           
            


