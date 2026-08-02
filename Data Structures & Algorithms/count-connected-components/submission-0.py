class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.res = 0
        visit = set()
        def dfs(n, parent):
            if n in visit:
                return
            visit.add(n)
            if parent == -1:
                self.res += 1
            for nei in adj[n]:
                dfs(nei, n)
        
        for i in range(n):
            dfs(i, -1)
        return self.res
        