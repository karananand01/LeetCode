class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        n =1
        res.append(1)
        while n< len(nums):
            res.append(res[n-1]*nums[n-1])
            n+=1
        right=1
        n=len(nums)-1
        while n>=0:
            res[n]=res[n]*right
            right=right*nums[n]
            n-=1
        return res