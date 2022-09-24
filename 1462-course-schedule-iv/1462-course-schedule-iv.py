from numpy import array
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[[0 for _ in range(numCourses)] for __ in range(numCourses)]
        for item in prerequisites:
            a,b=item
            graph[a][b]=1
        # print(array(graph))
        visited=[False for _ in range(len(graph))]
        # print(array(graph))
        for i in range(len(graph)):
            # print("NEW : ",i)
            self.get(graph,visited,i)
        ans=[]
        # print(array(graph))
        for q in queries:
            i,j=q
            if(graph[i][j]==1):
                ans.append(True)
            else:
                ans.append(False)
        return ans
    def get(self,graph,visited,node):
        if(not visited[node]):
            # print(node,graph[node])
            visited[node]=True
            for i in range(len(graph)):
                if(graph[node][i]==1):
                    self.get(graph,visited,i)
                    for j in range(len(graph)):
                        if(graph[i][j]==1):
                            graph[node][j]=1