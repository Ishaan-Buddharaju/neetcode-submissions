class UnionFind:
    # quick union with path compression
    def __init__(self, n):
        # start with self parents
        # index is the node being represented
        self.parents = [i for i in range(n)] 
        self.rank = [0 for i in range(n)]
        self.count = n

    def find(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, n1, n2):
        n1 = self.find(n1)
        n2 = self.find(n2)
        if n1 == n2:
            return
        
        if self.rank[n1] > self.rank[n2]: 
            # join n2 tree to n1
            self.parents[n2] = self.parents[n1]
        elif self.rank[n2] > self.rank[n1]: 
            # join n1 tree to n2
            self.parents[n1] = self.parents[n2]
        else: 
            self.parents[n1] = self.parents[n2]
            self.rank[n2] += 1
        self.count -= 1



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # graph = {i: [] for i in range(n)}
        # for edge in edges: 
        #     graph[edge[0]].append(edge[1])
        #     graph[edge[1]].append(edge[0])

        
        # visited = set()

        # def dfs(vertex):
        #     if vertex in visited:
        #         return 
        #     visited.add(vertex)
        #     for v in graph[vertex]:
        #         dfs(v)
        # components = 0
        # for vertex in graph:
        #     if vertex not in visited:
        #         components += 1
        #         dfs(vertex)

        # return components

        # DISJOIN SET
        components = UnionFind(n)
        componentCount = 0
        for edge in edges:
            components.union(edge[0], edge[1])
        return components.count
            
            
            