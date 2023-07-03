#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		stack=[]
	    for i in range(n):
	        if(len(stack)==0 or arr[stack[-1]]>arr[i]):
	            stack.append(i)
	    ans=-1
	    for i in range(n-1,-1,-1):
	        while(len(stack)!=0 and arr[stack[-1]]<=arr[i]):
	            ans=max(ans,i-stack.pop())
	    return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends