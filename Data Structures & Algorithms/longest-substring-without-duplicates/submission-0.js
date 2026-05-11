class Solution {
    /**
     * @param {string} s
     * @return {number}
     * 
     */
    lengthOfLongestSubstring(s) {
        let left = 0;
        let maxLength = 0;
        let set = new Set();
        for (let right = 0; right < s.length; right ++) {
            while (set.has(s[right])) {
                set.delete(s[left]) //maintains invariant that sliding window contains longest substring
                left ++;
            }
            set.add(s[right])
            maxLength = Math.max(maxLength, right - left + 1); //maintains invariant that maxLength contains the max length after the ith iteration
        }
        return maxLength;

    }
}
