from typing import List


class Solution:
    def totalCuts(self, N : int, k : int, A : List[int]) -> int:
        m=[]
        for item in A:
            if(len(m)==0):
                m.append(item)
            else:
                m.append(max(item,m[-1]))
        mr=[]
        for item in A[::-1]:
            if(len(mr)==0):
                mr.append(item)
            else:
                mr.append(min(item,mr[-1]))
        mr.reverse()
        ans=0
        for i in range(N-1):
            if(m[i]+mr[i+1]>=k):ans+=1
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
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends