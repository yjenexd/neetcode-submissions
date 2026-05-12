class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        startingElements = []
        maxCount = 0

        for num in numSet:
            if num - 1 not in numSet:
                startingElements.append(num)
        
        for startElem in startingElements:
            counter = 0
            currNum = startElem
            while currNum in numSet:
                counter += 1
                currNum += 1
            maxCount = max(maxCount, counter)
        
        return maxCount
            

        


#hash the entire array
#identify starting elements, in this case 2 and 10 because there does not exist element, create a list of starting elements
#find max consequtive