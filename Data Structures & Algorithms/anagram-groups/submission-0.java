class Solution{
    public List<List<String>> groupAnagrams(String[] strs) { //access modifier// return type, method name, parameters
        Map<String, List<String>> anagram = new HashMap<>();
        for (String s: strs){ // for string s in strs
            int[] count  = new int[26]; //initialize an array of int
            for (char c: s.toCharArray()){ //must convert string to char array
                count[c - 'a']++; //for char is single quotations
            }
            String key = Arrays.toString(count); //convert the array into a string.
            if (!anagram.containsKey(key)){ //use the containsKey method to check 
                anagram.put(key, new ArrayList<String>()); //create new list as value
                anagram.get(key).add(s); // add string in the value list
            }
            else{
                anagram.get(key).add(s); //get the value and add the string inside
            }
        }
        List<List<String>> result = new ArrayList<>(anagram.values());
        return result;
}
}

