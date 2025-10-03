class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        ones=0
        queue=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ones+=1
                elif grid[i][j]==2:
                    queue.append([i,j])
        if ones==0:
            return 0
        print("current queue",queue)
        while len(queue)>0:
            arrange=0
            n=len(queue)
            k=0
            while k<n:
                node=queue.pop(0)
                print("popped node",node)
                i,j=node[0],node[1]
                #check left 
                if j>0 and grid[i][j-1]==1:
                    arrange=1
                    grid[i][j-1]=2
                    queue.append([i,j-1])
                    #print("value appended 1")
                    ones-=1
                #check right
                if j+1<len(grid[0]) and grid[i][j+1]==1:
                    arrange=1
                    grid[i][j+1]=2
                    queue.append([i,j+1])
                    #print("value appended 2")
                    ones-=1
                #check up 
                if i>0 and grid[i-1][j]==1:
                    arrange=1
                    grid[i-1][j]=2
                    queue.append([i-1,j])
                    #print("value appended 3")
                    ones-=1
                #check down 
                if i+1<len(grid) and grid[i+1][j]==1:
                    arrange=1
                    grid[i+1][j]=2
                    queue.append([i+1,j])
                    #print("value appended 4")
                    ones-=1
                k+=1
            if arrange==1:
                time+=1
            print("queue and time currently",queue,time)
        print("number of ones is",ones)
        if ones==0:
            return time
        return -1



            

        