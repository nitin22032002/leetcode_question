#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        dp=[-1 for _ in range(N+1)]
        dp[0]=1
        dp[1]=1
        mod=10**8
        for i in range(2,N+1):
            dp[i]=(dp[i-1]+dp[i-2])%(mod)
        return dp[N]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends