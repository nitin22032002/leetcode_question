

from typing import List
class Solution:
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        s=sum(arr)
        vals=[]
        i=1
        while(i*i<=s):
            if(s%i==0):
                if(i>=K):
                    vals.append(s//i)
                if((s//i)>=K):
                    vals.append(i)
            i+=1
        vals.sort(reverse=True)
        for item in vals:
            if(self.get(arr,K,N,item)):return item
    def get(self,arr,K,N,item):
            s=0
            i=0
            while(i<N and K>0):
                s+=arr[i]
                if(K!=1 and s%item==0):
                    K-=1
                    s=0
                    if(i==N-1):K+=1
                i+=1
            if(s%item==0 and K==1):
                return True
            return False
        



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
        
        
        K = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, K, arr)
        
        print(res)
        

# } Driver Code Ends