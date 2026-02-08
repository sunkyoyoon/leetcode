class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        seen = {} 

        def dfs(crs):
            if crs in seen:
                return seen[crs]
            seen[crs] = True 
            for nei in premap[crs]:
                if dfs(nei):
                    return True
            seen[crs] = False 


        for crs in range(numCourses):
            if dfs(crs):
                return False 
        
        return True 
