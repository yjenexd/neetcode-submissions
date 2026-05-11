class Solution {
    public boolean hasDuplicate(int[] nums) {
        return Arrays.stream(nums).distinct().count() < nums.length;
        //make array into hashmap, then compare length;
    }
}