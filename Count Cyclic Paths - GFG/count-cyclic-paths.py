#User function Template for python3

class Solution:
    def countPaths (self, N):
        mod=int(1e9+7)
        a,b=1,0
        for i in range(1,N+1):
            a,b=(3*b)%mod,((2*b)%mod+(a)%mod)%mod
        return a
        


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