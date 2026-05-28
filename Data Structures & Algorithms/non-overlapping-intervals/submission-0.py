class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        new_intervals = sorted(intervals, key = lambda x: x[0])
        curr_max = new_intervals[0][1]
        for interval in new_intervals[1:]:
            if interval[0] < curr_max:
                counter += 1 ##represents deleting the longer one
                curr_max = min(curr_max, interval[1])
            else: ##no overlap
                curr_max = interval[1]
        return counter
            
