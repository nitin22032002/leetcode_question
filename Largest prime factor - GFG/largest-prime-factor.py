#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        ans=1
        i=2
        while(i*i<=N):
            while(N%i==0):
                ans=max(i,ans)
                N//=i
            i+=1
        ans=max(ans,N)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends