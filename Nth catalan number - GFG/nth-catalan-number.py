
class Solution:
    def findCatalan(self, n : int) -> int:
        dp=[0 for _ in range(n+1)]
        dp[1]=dp[0]=1
        mod=int(1e9+7)
        for i in range(2,n+1):
            j=0
            k=i-1
            while(j<i):
                dp[i]+=(dp[j]*dp[k])
                j+=1
                k-=1
                dp[i]%=mod
        return dp[-1]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends