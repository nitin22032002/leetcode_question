#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        dp=[0 for _ in range(n+1)]
        arr=[x,y,z]
        arr.sort()
        for item in arr:
            if(n<item):
                break
            dp[item]=1
        for item in arr:
            for i in range(item+1,n+1):
                if(dp[i-item]==0 or dp[item]==0):
                    continue
                dp[i]=max(dp[i],dp[i-item]+dp[item])
        return dp[n]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends