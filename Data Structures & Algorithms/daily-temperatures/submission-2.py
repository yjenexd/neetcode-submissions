class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures): #index and temperature
            if not stack or t <= stack[-1][1]:
                stack.append((i, t))
            elif t > stack[-1][1]:
                while stack and t > stack[-1][1]:
                    elem = stack.pop()
                    dist = i - elem[0]
                    res[elem[0]] = dist
                stack.append((i,t))
        return res
            

        