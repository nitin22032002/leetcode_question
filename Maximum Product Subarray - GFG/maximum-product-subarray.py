#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
	    i=0
	    p=1
	    isZero=False
	    first=1
	    ans=0
	    while(i<n):
	        if(arr[i]==0):
	           # print(first,p)
	            if(first!=1 and first!=p):
	                ans=max(ans,p//first)
	            p=1
	            isZero=True
	            first=1
	        else:
	            p*=arr[i]
	            if(ans==0):
	                ans=p
	            else:
	                ans=max(ans,p)
	            if(p<0 and first>0):
	                first*=p
	        i+=1
	    if(first!=1 and first!=p):
	        ans=max(ans,p//first)
	    if(ans<0 and isZero):
	        return 0
	    return ans
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends