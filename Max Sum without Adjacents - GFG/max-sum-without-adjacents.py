#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		dp=[0 for _ in range(n)]
		dp[0]=arr[0]
		if(n>1):
		    dp[1]=max(arr[1],dp[0])
		for i in range(2,n):
		    dp[i]=max(dp[i-2]+arr[i],dp[i-1])
		return dp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends