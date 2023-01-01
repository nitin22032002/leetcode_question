#User function Template for python3
from math import factorial
class Solution:
	def compute_value(self, n):
		r=factorial(2*n)//(factorial(n)**2)
		r%=((10**9)+7)
		return (r)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.compute_value(n)
		print(ans)
# } Driver Code Ends