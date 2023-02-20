#User function Template for python3
import sys
sys.setrecursionlimit(10**7)
class Solution:
    def countPaths (self, N):
        self.mod=int(1e9+7)
        a,b=1,0
        for i in range(1,N+1):
            c=3*b
            d=2*b+a
            c%=self.mod
            d%=self.mod
            a,b=c,d
        # print(dp)
        return a
        # return self.get(N,0,dp)
    def get(self,N,current,dp):
        s=0
        if(current!=0):
            s=1
        if(N==0):
            if(current==0):
                return 1
            return 0
        elif(dp[N][s]!=-1):
            return dp[N][s]
        else:
            ans=0
            if(s==0):
                pass
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.countPaths(N))

# } Driver Code Ends