class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        if num==1:
            return True
        while i<int(num/2)+1:
            if i*i>2**31-1:
                return False
            if i*i==num:
                return True
            i+=1
        return False
        