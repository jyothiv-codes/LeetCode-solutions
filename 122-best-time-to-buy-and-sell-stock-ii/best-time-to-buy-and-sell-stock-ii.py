class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        left=0
        right=1
        m=0
        s=0
        while right<len(prices):
            print(m,prices[left],prices[right])
            if prices[left]<prices[right]:
                m=prices[right]-prices[left]
                s+=m
                left+=1
            else:
                left=right
            right+=1
        return s
        