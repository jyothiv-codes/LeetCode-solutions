class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        makezero=[]
        rows=len(matrix)
        cols=len(matrix[0])
        zerorow=[0]*rows
        zerocol=[0]*cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    pair=[i,j]
                    makezero.append(pair)
        print(makezero)
        for pair in makezero:
            i=pair[0]
            j=pair[1]
            print(i,j)
            #make col 0
            for ni in range(rows):
                if matrix[ni][j]!=0:
                    matrix[ni][j]=0
            #make row 0
            for k in range(cols):
                if matrix[i][k]!=0:
                    matrix[i][k]=0
        

        