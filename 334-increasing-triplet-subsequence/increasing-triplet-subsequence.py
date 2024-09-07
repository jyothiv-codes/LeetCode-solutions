class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i=0
        first,second=2**31,2**31
        for i in nums:
            if i<=first:
                first=i
            elif i<=second:
                second=i
            elif i>second:
                return True
        return False

