#User function Template for python3
class Solution:
    def check(self, n, m, edges): 
        visited=[False for _ in range(n+1)]
        graph=[[] for _ in range(n+1)]
        
        for item in edges:
            a,b=item
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)
        for i in range(1,n+1):
            if(self.get(graph,i,visited,n-1)):
                return True
        return False
    def get(self,graph,node,visited,n):
        if(visited[node]):
            return False
        elif(n==0):
            return True
        else:
            visited[node]=True
            for item in graph[node]:
                if(self.get(graph,item,visited,n-1)):
                    return True
            visited[node]=False
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends