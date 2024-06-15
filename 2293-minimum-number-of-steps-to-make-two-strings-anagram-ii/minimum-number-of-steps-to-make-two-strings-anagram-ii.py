class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        d1={}
        d2={}
        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        for ch in t:
            d2[ch]=d2.get(ch,0)+1
        count=0
        for key in d1:
            if key in d2:
                count+=abs(d1[key]-d2[key])
            else:
                count+=d1[key]
        for key in d2:
            if key not in d1:
                count+=d2[key]
        return count


        