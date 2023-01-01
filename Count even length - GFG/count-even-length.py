#User function Template for python3
from math import factorial
class Solution:
	def compute_value(self, n):
		r1=1
		r2=1
		mod=(10**9)+7
		for i in range(1,2*n+1):
		    r1*=i
		    r1%=mod
		    if(i<=n):
		        r2*=i
		        r2%=mod
		
		r2=pow(r2,2,mod)
		r2=pow(r2,mod-2,mod)
		return (r1*r2)%mod


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