class Solution:
    def totalMoney(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            if i%7==1 and i!=1:
                dp[i]=dp[i-7]+1
            else:
                dp[i]=dp[i-1]+1
        print(dp)
        return sum(dp)


        