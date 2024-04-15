class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        m=0
        element=10**6
        for i in nums:
            if i%2==0:
                d[i]=d.get(i,0)+1
                if d[i]>m:
                    m=d[i]
                    element=i
                elif d[i]==m:
                    if i<element:
                        element=i
        if element==10**6:
            return -1
        else:
            return element

        