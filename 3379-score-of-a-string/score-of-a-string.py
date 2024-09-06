class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_=0
        for i in range(len(s)-1):
            diff=abs(ord(s[i])-ord(s[i+1]))
            sum_+=diff
        return sum_
        