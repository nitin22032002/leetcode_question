from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        A.sort(key=lambda x:[x%2,x])
        B.sort(key=lambda x:[x%2,x])
        a1=0
        b1=0
        # print(A,B)
        for i in range(N):
            if(A[i]%2!=B[i]%2):
                return -1
            else:
                if(A[i]!=B[i]):
                    if(B[i]>A[i]):
                        a1+=B[i]-A[i]
                    else:
                        b1+=A[i]-B[i]
        if(a1!=b1):
            return -1
        return a1//2


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
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends