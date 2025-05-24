class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for edge in edges:
            from_=edge[0]
            to_=edge[1]
            if from_ not in graph:
                graph[from_]=[]
            if to_ not in graph:
                graph[to_]=[]
            graph[from_].append(to_)
            graph[to_].append(from_)
        queue=collections.deque([source])
        visited=[False]*n
        visited[source]=True
        while queue:
            curr=queue.popleft()
            if curr==destination:
                return True
            for node in graph[curr]:
                if visited[node]!=True:
                    visited[node]=True
                    queue.append(node)
        return False


        