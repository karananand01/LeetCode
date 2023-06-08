class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while len(flowerbed)>i:
            if(n<=0):
                return True
            if i==0:
                if(len(flowerbed)>1):
                    if(flowerbed[i]==0 and flowerbed[i+1]==0):
                        flowerbed[i]=1
                        n-=1
                else:
                    if(flowerbed[i]==0):
                        flowerbed[i]=1
                        n-=1
                i+=1
                continue
            if i==len(flowerbed)-1:
                if(len(flowerbed)>1):
                    if(flowerbed[i]==0 and flowerbed[i-1]==0):
                        flowerbed[i]=1
                        n-=1
                else:
                    if(flowerbed[i]==0):
                        flowerbed[i]=1
                        n-=1
                i+=1
                continue
            if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
            i+=1
        if n>0:
            return False
        return True