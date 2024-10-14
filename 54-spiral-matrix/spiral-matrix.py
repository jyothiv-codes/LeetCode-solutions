class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        direction_index=0
        output=[]
        
        rows=len(matrix)
        cols=len(matrix[0])
        visited=[[False for y in range(cols)] for x in range(rows)]
        print(visited)
        i=0
        j=0
        for x in range(rows*cols):
            output.append(matrix[i][j])
            visited[i][j]=True
            ni=i+direction[direction_index][0]
            nj=j+direction[direction_index][1]
            if (ni<rows and nj<cols) and (ni>=0 and nj>=0) and visited[ni][nj]==False:
                i=ni
                j=nj
                   
            else:
                print("change direction")
                direction_index=(direction_index+1)%4
                i+=direction[direction_index][0]
                j+=direction[direction_index][1]
                
        return output




        