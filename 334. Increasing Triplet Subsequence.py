import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = sys.maxsize
        mid = sys.maxsize
        for x in nums:
            if x<left:
                left=x
            elif x<mid and x>left:
                mid=x
            elif x>mid and x>left:
                return True
        return False

