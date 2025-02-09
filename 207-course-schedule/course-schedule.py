from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses=defaultdict(list)
        indegree=[0]*numCourses
        queue = deque()
        for course,prereq in prerequisites:
            courses[prereq].append(course)
        for a,_ in prerequisites:
            indegree[a]+=1
        for c in range(numCourses):
            if indegree[c]==0:
                queue.append(c)
        while len(queue)>0:
            node=queue.popleft()
            for course in courses[node]:
                indegree[course]-=1
                if indegree[course]==0:
                    queue.append(course)
        print(indegree)
        print(queue)
        if sum(indegree)==0:
            return True
        return False

        