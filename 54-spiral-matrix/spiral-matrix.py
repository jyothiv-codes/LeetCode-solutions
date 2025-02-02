class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        traversal=[]
        rows=len(matrix)
        cols=len(matrix[0])
        ci=0
        cj=0
        direction_index=0
        visited=[]
        for k in range(rows*cols):
            traversal.append(matrix[ci][cj])
            visited.append([ci,cj])
            ni=ci+direction[direction_index][0]
            nj=cj+direction[direction_index][1]
            if ni>=0 and nj>=0 and ni<rows and nj<cols and [ni,nj] not in visited:
                ci=ni
                cj=nj
            else:
                direction_index=(direction_index+1)%4
                ci=ci+direction[direction_index][0]
                cj=cj+direction[direction_index][1]
        return traversal



        