# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        s=sum(arr)
        if(s%2!=0):
            return 0
        target=s//2
        return self.get(arr,0,target,{})
    def get(self,arr,i,s,dp):
        if(i>=len(arr)):
            if(s==0):return 1
            return 0
        elif((i,s) in dp):
            return dp[(i,s)]
        else:
            x=self.get(arr,i+1,s,dp)
            if(x==1):
                ans=1
            else:
                ans=self.get(arr,i+1,s-arr[i],dp)
            dp[(i,s)]=ans
            return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends