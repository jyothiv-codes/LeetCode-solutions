from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target==0:
            return True
        if x==0 or y==0:
            return target==x+y
        if x+y<target:
            return False
        return target%gcd(x,y)==0
        