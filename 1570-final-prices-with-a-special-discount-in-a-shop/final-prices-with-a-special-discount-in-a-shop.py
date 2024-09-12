class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices)==1:
            return prices
        i=0
        j=1
        subtract=[0]*len(prices)
        while i<len(prices):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    subtract[i]=prices[j]
                    break
            i+=1
        for i in range(len(prices)):
            subtract[i]=prices[i]-subtract[i]
        return subtract
        