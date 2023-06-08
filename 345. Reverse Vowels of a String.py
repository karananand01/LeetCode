class Solution:
    def reverseVowels(self, s: str) -> str:
        pos:int=[]
        vows=[]
        i=0
        for let in s:
            if let in {"a","e","i","o","u","A","E","I","O","U"}:
                pos.append(i)
                vows.append(let)
            i+=1
        
        vows.reverse()
        i=0
        for x in pos:
            s=s[:x]+vows[i]+s[x+1:]
            i+=1
        return s
        
