#User function Template for python3

class Solution:

	def findSubarray(self,a, n):
    	start=0
    	s=0
    	e=0
    	se=0
    	ans=0
    	for i in range(n):
    	    if(a[i]<0):
    	        if(ans<se):
    	            ans=se
    	            s=start
    	            e=i
    	        start=i+1
    	        se=0
    	    else:
    	        se+=a[i]
    	if(se>ans):
    	    s=start
    	    e=n
    	if(e==s):
    	    return [-1]
    	return a[s:e]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends