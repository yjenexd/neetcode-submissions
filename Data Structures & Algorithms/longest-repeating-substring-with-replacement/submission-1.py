class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #"XYYX", X:2, Y:2 #move the right pointer incrementally
        #if the lessfreq one is more than 2, move the left pointer
        #maintain a hashmap of letters within the sliding window
        j = 0
        window = {}
        max_len = 0
        for i in range (len(s)):
            window[s[i]] = 1 + window.get(s[i], 0)
            
            ##if the smaller number is more than k, we move the left pointer right
            while (i - j + 1) - max(window.values()) > k:
                window[s[j]] -= 1
                j += 1
            
            max_len = max(max_len, i - j + 1)
        return max_len


            
            

        