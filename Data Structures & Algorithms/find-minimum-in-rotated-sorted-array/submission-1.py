class Solution:
    def findMin(self, nums: List[int]) -> int: ##if middle larger than rightmose, search right, else search left
    #to leave one at the end make it inclusive inclusive
        low: int = 0
        high:int = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
                
            
        