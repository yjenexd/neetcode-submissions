class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums)
        curr_max, curr_min = 1, 1
        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
            else:
                tmp = curr_max * n
                curr_max = max(tmp, curr_min * n, n)
                curr_min = min(tmp, curr_min * n, n)
                global_max = max(curr_max, global_max)
        return global_max

        