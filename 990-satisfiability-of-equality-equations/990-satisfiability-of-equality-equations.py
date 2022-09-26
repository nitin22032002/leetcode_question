class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        state=[[0 for _ in range(26)] for __ in range(26)]
        for i in range(26):
            state[i][i]=1
        parent=[i for i in range(26)]
        rank=[0 for _ in range(26)]
        for item in equations:
            a,b,c,d=list(item)
            a=ord(a)-97
            d=ord(d)-97
            if(b=="!"):  
                val=2
            else:
                val=1
            p1=self.findParent(parent,a)
            p2=self.findParent(parent,d)
            # print(chr(p1+97),chr(p2+97),state[p1][p2],val)
            if((state[p1][p2]==0 or state[p1][p2]==val) and (state[p2][p1]==0 or state[p2][p1]==val)):
                if(val==1):
                    if(rank[p1]>rank[p2]):
                        parent[p2]=p1
                    elif(rank[p1]==rank[p2]):
                        parent[p1]=p2
                        rank[p2]+=1
                    else:
                        parent[p1]=p2
                    for i in range(26):
                        if(state[p2][i]!=0):
                            state[p1][i]=state[p2][i]
                        if(state[p1][i]!=0):
                            state[p2][i]=state[p1][i]
                state[p1][p2]=val
                state[p2][p1]=val
            elif(state[p1][p2]!=val):
                # print(chr(p1+97),chr(p2+97),state[p1][p2],val,state[p2][p1])
                return False
        return True
    
    def findParent(self,parent,node):
        if(parent[node]==node):
            return node
        parent[node]=self.findParent(parent,parent[node])
        return parent[node]