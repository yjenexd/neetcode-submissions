class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarysearch(arr, l, h, t):
            low = l
            high = h
            while low < high:
                mid = low + (high-low)//2
                if arr[mid] == t:
                    return mid
                elif arr[mid] < t:
                    low = mid + 1
                else:
                    high = mid
            return -1
            
        low = 0 #inclusive
        high = len(nums) #exclusive
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            ##standard check for sorted area, inclusive
            ##left is sorted
            elif nums[low] <= nums[mid - 1]:
                if target <= nums[mid - 1] and target >= nums[low]: ##sorted on left
                    return binarysearch(nums, low, mid, target)
                else: 
                    low = mid + 1
            ##right is sorted
            else: 
                if target <= nums[high - 1] and target >= nums[mid]:
                    return binarysearch(nums, mid + 1, high, target)
                else:
                    high = mid
        return -1 ##cannot find anything
    




        