#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    start=0
	    ans=0
	    curr=0
	    while(start<len(arr)-1):
	        t=start
	        while(curr<=t):
	            start=max(start,curr+arr[curr])
	            curr+=1
	        if(start<curr):return -1
	        ans+=1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends