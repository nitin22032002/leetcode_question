
from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        ans=-1
        s=sum(arr)
        i=1
        while(i*i<=s and i<=N):
            if(s%i==0):
                if((s//i)<=N):
                    return s//i
                ans=i
            i+=1
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
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMaximum(N, arr)
        
        print(res)
        

# } Driver Code Ends