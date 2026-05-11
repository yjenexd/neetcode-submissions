class Solution{
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length()) {return false;}
        HashMap<Character, Integer> s_hash = new HashMap<>();
        HashMap<Character, Integer> t_hash = new HashMap<>();
        for (int i = 0; i < s.length(); i++){
            if (s_hash.containsKey(s.charAt(i))){
                s_hash.put(s.charAt(i), s_hash.get(s.charAt(i)) + 1);
            }
            else{
                s_hash.put(s.charAt(i), 1);
            }
            if (t_hash.containsKey(t.charAt(i))){
                t_hash.put(t.charAt(i), t_hash.get(t.charAt(i)) + 1);
            }
            else{
                t_hash.put(t.charAt(i), 1);
            }
        }
        if (s_hash.equals(t_hash)){
            return true;
        }
        return false;
    }
}