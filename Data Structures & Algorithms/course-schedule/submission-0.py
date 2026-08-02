class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, req in prerequisites:
            preMap[crs].append(req)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False # Cycle
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for req in preMap[crs]:
                if not dfs(req): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
