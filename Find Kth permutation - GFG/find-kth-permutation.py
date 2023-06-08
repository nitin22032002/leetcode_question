#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List


from math import ceil
class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        par=[1]
        for i in range(2,n+1):
            par.append(par[-1]*i)
        par.reverse()
        visited=[False for _ in range(9)]
        ans=[]
        for i in range(1,n):
            r=ceil(k/par[i])
            t=r
            for j in range(9):
                if(r==1 and not visited[j]):
                    ans.append(str(j+1))
                    visited[j]=True
                    break
                elif(not visited[j]):r-=1
            k-=(t-1)*par[i]
        for i in range(9):
            if(not visited[i]):
                ans.append(str(i+1))
                break
        ans=int("".join(ans))
        return ans
        


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends