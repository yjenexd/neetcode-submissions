from functools import cache
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Helper function to find the max subarray ending EXACTLY at index i
        @cache
        def local_max(i: int) -> int:
            # Base case: The max subarray ending at index 0 is just nums[0]
            if i == 0:
                return nums[0]
            
            # Recursive step: Start a new subarray at i, OR extend the subarray ending at i-1
            return max(nums[i], nums[i] + local_max(i - 1))
        
        # The global max could end at ANY index, so we check all of them
        # We use a generator expression inside max() to evaluate local_max for every index
        return max(local_max(i) for i in range(len(nums)))