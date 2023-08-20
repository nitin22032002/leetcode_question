#User function Template for python3
from bisect import bisect_left,bisect_right
class Solution:

	def count(self,arr, n, x):
		j1=bisect_left(arr,x)
		j2=bisect_right(arr,x)
		return j2-j1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends