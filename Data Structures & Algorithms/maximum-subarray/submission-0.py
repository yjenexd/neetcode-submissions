class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max: int = nums[0]
        global_max: int = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num) ##should i extend my subarray or start a new one
            global_max = max(global_max, current_max)
        return global_max
        
#maxSubArray(arr(n)) == max(a[i], a[i] + maxSubArray[n - 1])