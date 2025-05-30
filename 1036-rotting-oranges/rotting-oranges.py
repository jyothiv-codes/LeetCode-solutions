from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        rows=len(grid)
        cols=len(grid[0])
        fresh_oranges=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    pair=[i,j]
                    rotten.append(pair)
                if grid[i][j]==1:
                    fresh_oranges+=1
        
        time=0
        nrot=0
        while len(rotten)>0:
            nrot=0
            current_rotten = rotten[:]
            rotten = []
            for pair in current_rotten:
                i,j=pair[0],pair[1]
                #look right 
                if j+1<cols:
                    if grid[i][j+1]==1:
                        new_rot=[i,j+1]
                        grid[i][j+1]=2
                        rotten.append(new_rot)
                        nrot+=1
                        fresh_oranges-=1
                # left 
                if j-1>=0:
                    if grid[i][j-1]==1:
                        new_rot=[i,j-1]
                        grid[i][j-1]=2
                        rotten.append(new_rot)
                        nrot+=1
                        fresh_oranges-=1
                # up 
                if i-1>=0:
                    if grid[i-1][j]==1:
                        new_rot=[i-1,j]
                        grid[i-1][j]=2
                        rotten.append(new_rot)
                        nrot+=1
                        fresh_oranges-=1

                #down 
                if i+1<rows:
                    if grid[i+1][j]==1:
                        new_rot=[i+1,j]
                        grid[i+1][j]=2
                        rotten.append(new_rot)
                        nrot+=1
                        fresh_oranges-=1
            
                #grid[i][j]=-1
                #rotten.pop(0)
            if len(rotten) > 0:
                time += 1
                print(grid)
                print("fresh oranges",fresh_oranges)
        print("fresh oranges",fresh_oranges)
        if fresh_oranges>0:
            return -1
        return time

            

        