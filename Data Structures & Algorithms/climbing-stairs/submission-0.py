from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int: #simple DP question
        if n < 1:
            return 0
        ##only one step, one way to reach the top
        if n == 1:
            return 1
        ##if there are two steps left, there are 2 ways to reach the top, 1 + 1 and 2
        elif n == 2:
            return 2
        ## n = 5
        else: #can either take 1 step or two steps
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
            
        ##caching is a tradeoff between time complexity and memory, use save time but you create memory in the hashmap to store the results of function
        