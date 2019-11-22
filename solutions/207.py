class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create graph
        graph = dict()
        for i in range(numCourses): graph[i] = set() #no graph[0]=[4,4]
        for p in prerequisites:
            if p[0] in range(numCourses) and p[1] in range(numCourses):
                graph[p[0]].add(p[1])
            else: 
                return False #n=2 p=[[3,7]]

        visited = [None for _ in range(numCourses)]
        for i in range(numCourses):
            if dfs(graph, visited, i): return False
        return True
        
def dfs(graph, visited, i):
    if visited[i] == 1: return True #1 = visiting
    if visited[i] == 2: return False  #2 = visited
    visited[i] = 1
    for j in graph[i]:
        if dfs(graph, visited, j):
            return True
    visited[i] = 2
    return False
