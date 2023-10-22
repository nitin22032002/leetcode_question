#User function Template for python3

class Solution:
    def numberOfPaths (self, M, N):
        x=M+N-2
        mod=int(1e9+7)
        p1=1
        p2=1
        for i in range(1,M):
            p1*=i
            p1%=mod
            p2*=(x-i+1)
            p2%=mod
        ans=p2*pow(p1,mod-2,mod)
        ans%=mod
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends