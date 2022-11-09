#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
	    return self.get(arr,0,0,sum(arr),{})
	def get(self,arr,i,s,t,dp):
	    if(i>=len(arr)):
	        return abs(2*s-t)
	    elif((i,s) in dp):
	        return dp[(i,s)]
	    else:
	        ans= min(self.get(arr,i+1,s+arr[i],t,dp),self.get(arr,i+1,s,t,dp))
	        dp[(i,s)]=ans
	        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends