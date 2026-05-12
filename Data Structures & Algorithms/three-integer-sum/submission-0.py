class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        hashmap = {}
        for i in range(n):
            for j in range(i, n):
                diff = -(nums[i] + nums[j])
                if i != j and diff in hashmap and hashmap[diff] != i and hashmap[diff] != j:
                    triplet = sorted([nums[i], nums[j], diff])
                    res.add(tuple(triplet))
                if nums[j] not in hashmap:
                    hashmap[nums[j]] = j
        return list(res)


     

##store val as key and index as val for checking