class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i  = 0
        j = n - 1
        min_height = 0
        curr_volume = 0
        if i >= j:
            return 0
        while height[i] <= height[i + 1] & i < j:
            i += 1
        while height[j] <= height[j - 1] & i < j:
            j -= 1
        while i < j:
            min_height = max(min_height, min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
                print(max(min_height - height[i], 0))
                curr_volume += max(min_height - height[i], 0)
            else:
                j -= 1
                print(max(min_height - height[j], 0))
                curr_volume += max(min_height - height[j], 0)
        return curr_volume

        
        

##maintain two pointers left and right
##greedily sum up the volume
##move the right pointer and left pointer the same way as perviously
##sum up all volume along the way, based of the minimum current height
