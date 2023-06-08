class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        i=0
        while(len(word1)>i and len(word2)>i):
            merged+=word1[i]
            merged+=word2[i]
            i+=1
        merged+=word1[i:]
        merged+=word2[i:]
        return merged