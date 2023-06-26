#User function Template for python3

class Solution:
    def nCr(self, n, r):
        r=min(r,n-r)
        return self.get(n,r,{})
    def get(self,n,r,dp):
        if(r>n or r<0):
            return 0
        elif(r==0 or r==n):
            return 1
        elif((n,r) in dp):
            return dp[(n,r)]
        else:
            x=self.get(n-1,r,dp)+self.get(n-1,r-1,dp)
            x%=(int(1e9+7))
            dp[(n,r)]=x
            return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends