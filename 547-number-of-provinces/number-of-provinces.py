class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def DFS(node):
            for neighbour in d[node]:
                if visited[neighbour]==False:
                    visited[neighbour]=True
                    DFS(neighbour)
        d={}
        n=len(isConnected)
        i=0
        count=0
        for row in isConnected:
            d[i]=[]
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    d[i].append(j)
            i+=1
        print(d)
        visited=[False]*n
        for key in d:
            if visited[key]==False:
                count+=1
                visited[key]=True
                DFS(key)
        return count
                    
                
        