#User function Template for python3

class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        par=[i for i in range(n+1)]
        rank=[0 for _ in range(n+1)]
        ans=[]
        for a,b in mix:
            r1=self.find(par,a)
            r2=self.find(par,b)
            for a1,b1 in danger:
                p1=self.find(par,a1)
                p2=self.find(par,b1)
                if((p1==p2) or (p1==r1 and p2==r2) or (p1==r2 and p2==r1)):
                    ans.append("No")
                    break
            else:
                self.union(a,b,par,rank)
                ans.append("Yes")
        return ans
    def union(self,node1,node2,par,rank):
        p1=self.find(par,node1)
        p2=self.find(par,node2)
        if(p1!=p2):
            if(rank[p1]>rank[p2]):
                par[p2]=p1
            elif(rank[p2]>rank[p1]):
                par[p1]=p2
            else:
                par[p1]=p2
                rank[p2]+=1
        return p1,p2
    def find(self,par,node):
        if(par[node]==node):
            return node
        par[node]=self.find(par,par[node])
        return par[node]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        mix = [[0 for _ in range(2)] for _ in range(n)]
        danger = [[0 for _ in range(2)] for _ in range(m)]
        for i in range(n+m):
            if i < n:
                a,b = map(int, input().split())
                mix[i][0] = a
                mix[i][1] = b
            else:
                a,b = map(int, input().split())
                danger[i-n][0] = a
                danger[i-n][1] = b
        
        obj=Solution()
        print(*obj.avoidExlosion(mix, n, danger, m))
        
# } Driver Code Ends