class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left=0
        right=1
        m=0
        while right<len(prices):
            if prices[left]<prices[right]:
                m=max(m,prices[right]-prices[left])
            else:
                left=right
            right+=1
        return m
        