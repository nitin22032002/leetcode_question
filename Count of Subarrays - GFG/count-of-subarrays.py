#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):
	    i=0
	    ans=0
	    start=-1
	    while(i<n):
	        if(arr[i]>k):
	            ans+=(i+1)
	            start=i
	        else:
	           #if(start!=-1):
	           ans+=(start+1)
	        i+=1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends