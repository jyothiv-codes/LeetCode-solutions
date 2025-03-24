class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d={}
        def dfs(node,d,connected):
            if visited[node]==True:
                return 
            visited[node]=True
            connected.append(node)
            if node in d:
                for neighbour in d[node]:
                    if visited[neighbour]==False:
                        dfs(neighbour,d,connected)
        for edge in edges:
            from_=edge[0]
            to_=edge[1]
            if from_ not in d:
                d[from_]=[]
            if to_ not in d:
                d[to_]=[]
            d[from_].append(to_)
            d[to_].append(from_)

        print(d)
        i=0
        count=0
        visited=[False]*n
        for i in range(n):
            if visited[i]==False:
                #count+=1
                connected=[]
                dfs(i,d,connected)
                print(connected)
                len_nodes=len(connected)
                len_edges=0
                for node in connected:
                    if node in d:
                        len_edges+=len(d[node])
                #print("node and edges",len_nodes,len_edges)
                if (len_edges/2)==len_nodes*(len_nodes-1)/2:
                    count+=1
        return count


        