#User function Template for python3

class Solution:
	def is_bleak(self, n):
		bits=self.bits(n)
		for i in range(bits+1):
		    if(self.set_bit(n-i)==i):
		        return 0
		return 1
	def bits(self,n):
	    ans=0
	    while(n!=0):
	        ans+=1
	        n//=2
	    return ans
	def set_bit(self,n):
	    ans=0
	    while(n!=0):
	        ans+=n%2
	        n//=2
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends