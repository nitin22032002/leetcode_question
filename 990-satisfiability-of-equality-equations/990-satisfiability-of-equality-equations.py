class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent=[i for i in range(26)]
        rank=[0 for _ in range(26)]
        for item in equations:
            a,b,c,d=list(item)
            a=ord(a)-97
            d=ord(d)-97
            p1=self.findParent(parent,a)
            p2=self.findParent(parent,d)
            if(p1!=p2 and b=="="):
                self.union(parent,p1,p2,rank)
        for item in equations:
            a,b,c,d=list(item)
            a=ord(a)-97
            d=ord(d)-97
            p1=self.findParent(parent,a)
            p2=self.findParent(parent,d)
            if(p1==p2 and b=="!"):
                return False
                
        return True
    
    def findParent(self,parent,node):
        if(parent[node]==node):
            return node
        parent[node]=self.findParent(parent,parent[node])
        return parent[node]
    def union(self,parent,node1,node2,rank):
        if(rank[node1]==rank[node2]):
            parent[node1]=node2
            rank[node2]+=1
        elif(rank[node1]>rank[node2]):
            parent[node2]=node1
        else:
            parent[node1]=node2