class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res


##i want to encode the list of strings, in a most time efficient way, O(N) should be efficient
#to encode, append length of word, then the char in the words, then a special # that we would then skip
5#Hello5#World find the # then do whatever after
