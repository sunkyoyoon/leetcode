class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = [0] * numCourses   # 0=unvisited, 1=visiting, 2=visited
        ans = []

        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            
            visited[node] = 1
            for v in graph[node]:
                if dfs(v):
                    return True
            visited[node] = 2 
            ans.append(node)

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return []
        return ans[::-1]




