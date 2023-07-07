class Solution:
    def compress(self, chars) -> int:
        curr=""
        leng=0
        temp=""
        for x in chars:
            if x!=curr:
                if leng>1:
                    temp+=str(leng)
                temp+=x
                curr=x
                leng=1
            else:
                leng+=1
        
        if leng>1:
            temp+=str(leng)
        for i in range(0,len(temp)):
            chars[i]=temp[i]
        return len(temp)

sol = Solution()
print(sol.compress(["a","a","b","b","c"]))