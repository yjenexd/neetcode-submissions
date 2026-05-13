class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        width = n - 1
        max_volume = 0
        while i < j:
            max_volume = max(max_volume, width * min(heights[i], heights[j]))
            if (heights[i] < heights[j]):
                i += 1
                width -= 1
            else :
                j -= 1
                width -= 1
        return max_volume








##maintain one pointer to the left and one pointer to the right
##for the left pointer, increment if the height on the right is greater than the height on the left
##for the right pointer, decrement it if the height on the left is greater than the heigh on the right
##maintain a current length. 

##this will not work because a side can be a decrease followed by a great increase

##naively O(n^2) solution where i just find all the possible volumes and output the maximum one with all possibilities
##O(N) i just recalculate the volume everytime i decrement of increment

##maintain a max volume
##gredily increment left or right based on the smaller one

##proof
## lets say we keep the smaller height and move the taller height. the width decreases and the height is capped by the smaller height
##however this does not maximise the volume we have seen so far
##contrast this with keeping the taller height, the height is capped by the taller height, so it still maximises the volume we have seen so far
##proof by contradiction