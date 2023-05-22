from typing import List


class Solution:
    def solve(self, N : int, p : List[int]) -> int:
        tree=[[] for _ in range(N)]
        for i in range(N):
            if(p[i]!=-1 and p[i]!=i):
                tree[p[i]].append(i)
                tree[i].append(p[i])
        visited=[False]*N
        ans=0
        for i in range(N):
            if(not visited[i]):
                a,b=self.get(tree,i,visited)
                if(len(tree[i])>1):
                    b+=1
                # print((i,a,b))
                ans+=(a-b+1)
        return max(ans-1,0)
    def get(self,tree,node,visited):
        if(visited[node]):
            return [0,0]
        else:
            visited[node]=True
            ans=[1,0]
            for item in tree[node]:
                if(item==node):
                    continue
                a,b=self.get(tree,item,visited)
                ans[0]+=a
                ans[1]+=b
            if(len(tree[node])<=1):
                ans[1]+=1
            return ans
        



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
        
        
        p=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, p)
        
        print(res)
        

# } Driver Code Ends