class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        ans=[]
        for candy in candies:
            if extraCandies+candy>=m:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        