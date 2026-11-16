from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # The order is a bfs starting at the sources
        # They are sources since I flip the edge orientation
        indegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        for edge in prerequisites: 
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        
        q = deque()
        for i in range(numCourses): 
            if indegree[i] == 0:
                q.append(i)

        result = []

        while q:
            curr = q.popleft()
            result.append(curr)
            for edge in graph[curr]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    q.append(edge)

        if len(result) != numCourses:
            return []

        return result
