class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[_ for _ in range(len(edges))]
        rank=[0 for _ in range(len(edges))]
        for item in edges:
            a,b=item
            p1=self.find(par,a-1)
            p2=self.find(par,b-1)
            if(p1==p2):
                return item
            self.union(par,p1,p2,rank)
        return [-1,-1]
    def find(self,par,node):
        if(node==par[node]):
            return node
        par[node]=self.find(par,par[node])
        return par[node]
    
    def union(self,par,p1,p2,rank):
        if(rank[p1]==rank[p2]):
            par[p1]=p2
            rank[p2]+=1
        elif(rank[p1]>rank[p2]):
            par[p2]=p1
        else:
            par[p1]=p2
        