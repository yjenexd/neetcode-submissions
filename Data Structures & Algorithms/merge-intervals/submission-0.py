class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        new_list = list(sorted(intervals, key = lambda x: x[0]))
        new_interval = new_list[0]
        for interval in new_list[1:]:
            if new_interval[1] < interval[0]:
                res.append(new_interval)
                new_interval = interval
            else:
                new_interval = [min(new_interval[0], interval[0]),
                max(new_interval[1], interval[1])]
        
        res.append(new_interval)
        return res
        
##rmb sort
##consider edge cases