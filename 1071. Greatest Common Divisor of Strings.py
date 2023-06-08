class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        ans=""
        i=0
        while len(str1)>i and len(str2)>i and str1[i]==str2[i]:
            gcd+=str1[i]
            i+=1
            if len(str1)% i==0 and len(str2)% i==0:
                    ans=gcd
        if(ans==""):
            return ""
        fact = int(len(str1)/len(ans))
        if ans*fact != str1:
            return ""
        
        fact = int(len(str2)/len(ans))
        if ans*fact != str2:
            return ""

        return ans
            