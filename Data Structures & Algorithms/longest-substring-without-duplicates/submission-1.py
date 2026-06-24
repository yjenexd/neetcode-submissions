class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

      seen = set()
      start = 0
      running_max = 0
      
      
      for end in range(len(s)):

        #if the current character is in seen, we will remove s[start]
        while s[end] in seen:
          seen.remove(s[start])
          start += 1

        #base case, add unique element
        seen.add(s[end])

        #update solution
        running_max = max(running_max, end - start + 1)

      return running_max