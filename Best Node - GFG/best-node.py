from typing import List


class Solution:
    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        graph=[[] for _ in range(N)]
        for i in range(len(P)):
            if(P[i]==-1):
                continue
            else:
                graph[P[i]-1].append(i)
        ans=[-1e9]
        self.get(graph,0,A,1,ans)
        return ans[0]
    def get(self,graph,node,value,state,ans):
        if(len(graph[node])==0):
            ans[0]=max(ans[0],value[node])
            return [state*value[node],state*value[node]]
        else:
            rMin=1e9
            rMax=-1e9
            for item in graph[node]:
                x=self.get(graph,item,value,state*-1,ans)
                rMin=min(rMin,x[0])
                rMax=max(rMax,x[1])
            rMin+=value[node]*state
            rMax+=value[node]*state
            if(state==1):
                ans[0]=max(ans[0],rMax)
            else:
                ans[0]=max(ans[0],-rMin)
            return [rMin,rMax]
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.bestNode(N, A, P)
        
        print(res)
        

# } Driver Code Ends