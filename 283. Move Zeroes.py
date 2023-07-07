class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes=0
        i=0
        while i <len(nums):
            if nums[i]==0:
                zeroes+=1
                nums.remove(0)
            else:
                i+=1
        for x in range(0,zeroes):
            nums.append(0)