class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # we first take a transpose 
        matrix=[[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                matrix[j][i]=grid[i][j]
        print("matrix",matrix)
        print("grid",grid)
        i=0
        count=0
        for i in range(rows):
            if grid[i] in matrix:
                count+=matrix.count(grid[i])
            print(i)
        return count
        