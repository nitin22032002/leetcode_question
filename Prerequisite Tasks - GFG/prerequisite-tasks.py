#User function Template for python3

class Solution:
    def isPossible(self,n,task):
        graph=[[] for _ in range(n)]
        for item in task:
            graph[item[1]].append(item[0])
        return not(self.cycle(graph))
    def cycle(self,graph):
        visited=[False for _ in range(len(graph))]
        dfs=[False for _ in range(len(graph))]
        for i in range(len(dfs)):
            if(not visited[i]):
                if(self.dfs(graph,i,visited,dfs)):
                    return True
        return False
    
    def dfs(self,graph,node,visited,dfs):
        if(dfs[node]):
            return True
        elif(visited[node]):
            return False
        else:
            visited[node]=True
            dfs[node]=True
            for item in graph[node]:
                if(self.dfs(graph,item,visited,dfs)):
                    return True
            dfs[node]=False
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends