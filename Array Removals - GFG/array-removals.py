#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
		arr.sort()
		i=0
		while(i<n):
		    if(arr[-1]-arr[i]<=k):
		        break
		    i+=1
		ans=i
		j=n-1
		i-=1
		while(j>=0 and i>=0):
		    if(arr[j]-arr[i]>k):
		        i-=1
		        j-=1
		    else:
		        ans=min(ans,i+n-j-1)
		        i-=1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends