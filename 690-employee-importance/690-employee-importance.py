"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph={}
        visited={}
        for item in employees:
            graph[item.id]=[item.importance,item.subordinates]
            visited[item.id]=False
        stack=[id]
        cost=0
        while(len(stack)!=0):
            top=stack.pop()
            cost+=graph[top][0]
            visited[top]=True
            for item in graph[top][1]:
                if(not visited.get(item,True)):
                    stack.append(item)
        return cost
            