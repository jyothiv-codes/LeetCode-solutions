class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=-10**5
        s=0
        for num in gain:
            s+=num
            m=max(m,s)
        return max(m,0)

        