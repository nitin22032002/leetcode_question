#User function Template for python3

class Solution:
    def countVertex(self, N, edges):
        graph=[[] for _ in range(N)]
        for a,b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        dp=[[-1,-1] for _ in range(N)]
        return self.get(graph,0,1,dp,-1)
    def get(self,graph,node,par,dp,p):
        if(dp[node][par]!=-1):
            return dp[node][par]
        else:
            if(par==1):
                a1=1
                a2=0
                for item in graph[node]:
                    if(item==p):continue
                    a1+=self.get(graph,item,1,dp,node)
                    a2+=self.get(graph,item,0,dp,node)
                cost=min(a1,a2)
            else:
                cost=1
                for item in graph[node]:
                    if(item==p):continue
                    cost+=self.get(graph,item,1,dp,node)
            dp[node][par]=cost
            return cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        edges=[]
        for _ in range(N-1):
            arr = list(map(int,input().split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(N, edges))
# } Driver Code Ends