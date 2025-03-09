from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def check_if_rotten(grid,i,j):
            if i<=rows-1 and j<=cols-1 and i>=0 and j>=0:
                if grid[i][j]==1:
                    grid[i][j]=2
                    return True
            return False
        total_fresh=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    pair=[i,j]
                    queue.append(pair)
                elif grid[i][j]==1:
                    total_fresh+=1
        count=0
        rotten=False
        rows=len(grid)
        cols=len(grid[0])
        while queue:
            rotten=False
            for k in range(len(queue)):
                node=queue.popleft()
                i=node[0]
                j=node[1]
                
                #check up
                if check_if_rotten(grid,i-1,j):
                    pair=[i-1,j]
                    queue.append(pair)
                    rotten=True
                    total_fresh-=1
                
                #check down
                if check_if_rotten(grid,i+1,j):
                    pair=[i+1,j]
                    queue.append(pair)
                    rotten=True
                    total_fresh-=1
                #check right
                if check_if_rotten(grid,i,j+1):
                    pair=[i,j+1]
                    queue.append(pair)
                    rotten=True
                    total_fresh-=1
                #check left
                if check_if_rotten(grid,i,j-1):
                    pair=[i,j-1]
                    queue.append(pair)
                    rotten=True
                    total_fresh-=1
            if rotten:
                count+=1
        print(grid,total_fresh)
        if total_fresh>0:
            return -1
        return count



        