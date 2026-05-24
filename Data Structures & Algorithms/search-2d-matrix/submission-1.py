class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ##binary search the rows array based on the largest element, find the correct row array
        ##run vanilla binary search on the array
        ##log(m) + log(n) = log(m * n)
        arr: List[int] = []
        low:int = 0
        high:int = len(matrix)
        while low < high:
            middle = low + (high - low) // 2
            if matrix[middle][-1] >= target and matrix[middle][0] <= target:
                arr = matrix[middle]
                break ##need break out or infinite loop
            elif matrix[middle][-1] < target: #narrow to higher search space
                low = middle + 1
            else:
                high = middle
        
        low, high = 0, len(arr)
        while low < high:
            middle = low + (high - low) // 2
            if arr[middle] == target:
                return True
            elif arr[middle] < target: 
                low = middle + 1
            else:
                high = middle
        return False

