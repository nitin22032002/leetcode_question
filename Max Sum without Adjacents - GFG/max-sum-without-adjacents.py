#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		a=arr[0]
		b=a
		if(n>1):
		    b=max(arr[1],a)
		for i in range(2,n):
		    c=max(a+arr[i],b)
		    a,b=b,c
		return b


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