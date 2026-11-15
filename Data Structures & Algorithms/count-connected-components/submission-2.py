# class UnionFind:
#     # quick find 
#     def __init__(self, n):
#         # start with self parents
#         # index is the node being represented
#         self.parents = [i for i in range(n)] 

#     def find(self, n):
#         return self.parents[n]
#     def union(self, n1, n2):





class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for edge in edges: 
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        
        visited = set()

        def dfs(vertex):
            if vertex in visited:
                return 
            visited.add(vertex)
            for v in graph[vertex]:
                dfs(v)
        components = 0
        for vertex in graph:
            if vertex not in visited:
                components += 1
                dfs(vertex)

        return components
            
            