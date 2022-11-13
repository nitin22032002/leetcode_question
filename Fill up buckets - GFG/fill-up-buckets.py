#User function Template for python3

class Solution:
	def totalWays(self, n, capacity):
		capacity.sort()
		ans=1
		mod=((10**9)+7)
		for i in range(n):
		    if(capacity[i]-i<=0):
		        return 0
		    else:
		        ans*=(capacity[i]-i)
		        ans%=mod
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		capacity = list(map(int,input().split()))
		ob = Solution()
		ans = ob.totalWays(n,capacity)
		print(ans)

# } Driver Code Ends