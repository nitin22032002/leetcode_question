#User function Template for python3

from queue import Queue
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        visited=[False]*V
        obj=Queue()
        obj.put([0,0])
        visited[0]=True
        while(not obj.empty()):
            cost,node=obj.get()
            if(node==X):
                return cost
            for item in adj[node]:
                if(not visited[item]):
                    obj.put([cost+1,item])
                    visited[item]=True
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends