class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=10**9
        rows=len(grid)
        cols=len(grid[0])
        dp=[[100**9 for y in range(cols)]for x in range(rows)]
        #print(dp)
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    #left
                    if j-1>=0:
                        dp[i][j]=min(dp[i][j],dp[i][j-1])
                    #up
                    if i-1>=0:
                        dp[i][j]=min(dp[i][j],dp[i-1][j])
                    dp[i][j]+=grid[i][j]
        print(dp)
        return dp[-1][-1]



        