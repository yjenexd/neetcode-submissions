class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res.append(1)
        for i in range(len(nums)):
            if (i == 0):
                continue
            res.append(res[i - 1] * nums[i - 1])

        right = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res



##naively i run through the array to find product, then for each number i divide the product by the number this is two pass
##first pass we populate array with products left of i
##seond pass we multiply each number with numbers right of i