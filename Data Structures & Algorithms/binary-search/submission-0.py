class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0  #inclusive of low, exclusive of high
        high = len(nums) #6
        while low < high:
            middle = low + (high - low) // 2
            print(middle)
            if (nums[middle] == target):
                return middle
            elif nums[middle] < target:
                low = middle + 1 
            else:
                high = middle
        return -1


        