class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        q = deque([(0, -1)])
        visited = set([0])
        while q:
            node, parent = q.popleft()
            for nei in adjList[node]:
                if nei != parent:
                    if nei in visited:
                        return False
                    else:
                        visited.add(nei)
                        q.append([nei, node])
        return len(visited) == n

        # adjList = [[1,2,3],[0,4],[0],[0],[1]]
        # q = [[1,0],[2,0],[3,0]], visited = [0,1,2,3]
        # q = [[2,0],[3,0],[4,1]], visited = [0,1,2,3,4]

        # adjList[[]]

