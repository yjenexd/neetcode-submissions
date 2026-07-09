class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ##candidates can be used multiple time
        ##unique if frequency of chose number is different
        res = []
        sorted_candidates = sorted(candidates)
        def helper(start, end, num, curr_nums):
            ##reach end of candidate list and never hit target
            #order of base case is wrong
            #if we have hit our target
            if num == 0:
                if curr_nums is not None:
                     res.append(curr_nums)
                return
            #if we no longer can hit target
            elif num < 0 or start >= end:
                return
            elif sorted_candidates[start] > num:
                return
            else:
                number = sorted_candidates[start]
                new_curr_nums = curr_nums + [number]
                helper(start, end, num - number, new_curr_nums) #take or dont take
                helper(start + 1, end, num, curr_nums)
                return
        helper(0, len(candidates), target, [])
        return res
        #unbounded knapsack