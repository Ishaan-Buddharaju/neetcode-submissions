class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        graph = {i: [] for i in range(numCourses)}
        for edge in prerequisites: 
            source = edge[0]
            if source == edge[1]:
                return False
            graph[source].append(edge)

        
        seen = set()
        visited = set()
        def dfs(course):
            if course in seen: 
                return False
            if course in visited:
                return True
            seen.add(course)
            for edge in graph[course]:
                path = dfs(edge[1])
                if not path: 
                    return False
            visited.add(course)
            seen.remove(course)
            return True

        for vertex in graph: 
            path = dfs(vertex)
            if not path: 
                return False
        return True

            
