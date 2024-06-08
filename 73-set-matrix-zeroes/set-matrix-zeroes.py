class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        r=len(matrix)
        
        c=len(matrix[0])
        modified=[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0 and [i,j] not in modified:
                    #modify the column
                    for k in range(r):
                        if matrix[k][j]!=0:
                            matrix[k][j]=0
                            modified.append([k,j])
                    #modify the row
                    for k in range(c):
                        if matrix[i][k]!=0:
                            matrix[i][k]=0
                            modified.append([i,k])
                    



                    """
                    if i in rows and j not in cols:
                        cols.append(j)
                        for k in range(r):
                            if matrix[k][j]!=0:
                                matrix[k][j]=0
                    elif i not in rows and j in cols:
                        rows.append(i)
                        for k in range(c):
                            if matrix[i][k]!=0:
                                matrix[i][k]=0
                    elif i not in rows and j not in cols:
                        cols.append(j)
                        for k in range(r):
                            if matrix[k][j]!=0:
                                matrix[k][j]=0
                        rows.append(j)
                        for k in range(c):
                            if matrix[i][k]!=0:
                                matrix[i][k]=0
                                """
