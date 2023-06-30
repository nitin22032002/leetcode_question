#User function Template for python3
class Solution:
	def isDivisible(self, s):
	    ans=0
		for i in range(len(s)-1,-1,-1):
		    if(s[i]=='1'):
		        if((len(s)-i-1)%2==0):
		            ans+=1
		        else:
		            ans+=2
		        ans%=3
		return int(ans==0)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends