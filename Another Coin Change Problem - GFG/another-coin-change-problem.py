from typing import List


class Solution:
    def makeChanges(self, N : int, K : int, target : int, coins : List[int]) -> bool:
        coins.sort()
        ans=self.get(coins,0,target,K,{})
        return ans
    def get(self,arr,i,target,k,dp):
        if(target==0):
            return k==0
        elif(k==0):
            return False
        elif((i,target,k) in dp):
            return dp[(i,target,k)]
        else:
            ans=False
            for j in range(i,len(arr)):
                if(arr[j]>target):
                    break
                ans=self.get(arr,j,target-arr[j],k-1,dp)
                if(ans):
                    break
            dp[(i,target,k)]=ans
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
        
        
        target = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.makeChanges(N, K, target, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends