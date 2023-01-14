#User function Template for python3

class Solution: 
    def luckyPermutations(self, N, M, arr, graph):
        ans=0
        d={}
        for item in arr:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        grph=[[] for _ in range(N)]
        for a,b in graph:
            grph[a-1].append(b-1)
            grph[b-1].append(a-1)
        dp=[[-1 for _ in range(1<<N)] for __ in range(N)]
        visited=[0 for _ in range(N)]
        for i in d:
            ans+=self.get(grph,i-1,N-1,visited,d,dp)
        return ans
    def get(self,graph,node,N,visited,d,dp):
        b=0
        bit=1
        for i in d:
            for j in range(visited[i-1]):
                b|=bit
                bit<<=1
            bit<<=(d[i]-visited[i-1])
        # print(visited)
        # print(b)
        if((node+1) not in d):
            return 0
        elif(N==0):
            return 1
        elif(dp[node][b]!=-1):
            return dp[node][b]
        else:
            visited[node]+=1
            ans=0
            for item in graph[node]:
                if(visited[item]<d.get(item+1,0)):
                    ans+=(self.get(graph,item,N-1,visited,d,dp)*(d[node+1]-visited[node]+1))
            visited[node]-=1
            dp[node][b]=ans
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0:
        N, M=[int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        graph = []
        for i in range(M):
            graph.append([int(i) for i in input().split()])
        ob = Solution()
        print(ob.luckyPermutations(N, M, arr,graph))
        
        T -= 1
# } Driver Code Ends