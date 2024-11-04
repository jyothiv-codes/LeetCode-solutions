from collections import OrderedDict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topoSort(i,d,visited,stack):
            visited[i]=-1
            if i in d:
                for node in d[i]:
                    if visited[node]==-1:
                        return True
                    if visited[node]==0:
                        if topoSort(node,d,visited,stack):
                            return True
            stack.append(i)
            visited[i]=1
            return False
        d=OrderedDict()
        for edge in prerequisites:
            to_=edge[0]
            from_=edge[1]
            if from_ not in d:
                d[from_]=[]
            d[from_].append(to_)
        for i in range(numCourses):
            if i not in d:
                d[i]=[]
        stack=[]
        print(d)
        visited=[0]*numCourses
        for i in range(numCourses):
            if visited[i]==0:
                if topoSort(i,d,visited,stack):
                    return []
        answer=stack[::-1]
        return answer
        
        


        