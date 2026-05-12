from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums)):
            # If the current value is greater than zero, we can't sum to zero 
            # because the array is sorted (everything to the right is bigger).
            if nums[i] > 0:
                break
            
            # Skip duplicate elements for the 'i' pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 2: Use Two Pointers for the remaining array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    # Sum is too big, decrease it by moving the right pointer left
                    right -= 1
                elif total < 0:
                    # Sum is too small, increase it by moving the left pointer right
                    left += 1
                else:
                    # We found a triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers to look for more combinations
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for the 'left' pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # (Optional) Skip duplicates for 'right' pointer too
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res

##store val as key and index as val for checking