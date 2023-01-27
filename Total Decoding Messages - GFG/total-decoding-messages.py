#User function Template for python3

class Solution:
	def CountWays(self, str):
		dp=[-1 for _ in range(len(str))]
	    return self.get(str,0,dp)
	def get(self,s,i,dp):
	    if(i>=len(s)):
	        return 1
	    elif(s[i]=='0'):
	       return 0
	    elif(dp[i]!=-1):return dp[i]
	    else:
	           ans=self.get(s,i+1,dp)
	           if(i+1<len(s) and int(s[i:i+2])<=26):
	               ans+=self.get(s,i+2,dp)
	           dp[i]=ans%int(1e9+7)
	           return dp[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends