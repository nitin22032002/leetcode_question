from queue import Queue
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d={}
        for i in range(len(equations)):
            a,b=equations[i]
            if(a not in d):
                d[a]=[]
            d[a].append([b,values[i]])
            if(b not in d):
                d[b]=[]
            d[b].append([a,1/values[i]])
        ans=[]
        # print(d)
        for item in queries:
            a,b=item
            ans.append(self.get(d,a,b))
        return ans
    def get(self,graph,start,end):
        if(start not in graph or end not in graph):
            return -1
        else:
            obj=Queue()
            obj.put([start,1])
            visited={item:False for item in graph}
            while(not obj.empty()):
                node,cost=obj.get()
                if(node==end):
                    return cost
                elif(visited[node]):
                    continue
                else:
                    visited[node]=True
                    for item in graph[node]:
                        obj.put([item[0],cost*item[1]])
            return -1
                