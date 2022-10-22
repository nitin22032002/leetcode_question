#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        a=0
        b=1
        mod=10**8
        for i in range(1,N+1):
            t=(a+b)%(mod)
            a=b
            b=t
        return b


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