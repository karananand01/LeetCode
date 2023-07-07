class Solution:
    def reverseWords(self, s: str) -> str:
        s=" "+s+" "
        words=[]
        word=""
        for chr in s:
            if chr==" ":
                if word!="":
                    words.append(word)
                word=""
            else:
                word+=chr
        words.reverse()
        return " ".join(words)
