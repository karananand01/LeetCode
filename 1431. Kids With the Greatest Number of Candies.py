class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great=candies[0]
        for cnd in candies:
            if cnd>great:
                great = cnd
        
        result=[]
        for cnd in candies:
            if cnd+extraCandies>=great:
                result.append(True)
            else:
                result.append(False)
        
        return result