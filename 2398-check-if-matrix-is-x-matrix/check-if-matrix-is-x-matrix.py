class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i==j or i+j+1==rows:
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]!=0:
                        return False
        return True
        