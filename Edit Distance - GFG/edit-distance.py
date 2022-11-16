class Solution:
	def editDistance(self, s, t):
	    dp=[[-1 for _ in range(len(t))] for __ in range(len(s))]
		return self.get(s,t,0,0,dp)
	def get(self,s,t,i,j,dp):
	    if(i>=len(s)):
	        return (len(t)-j)
	    elif(j>=len(t)):
	        return (len(s)-i)
	    elif(dp[i][j]==-1):
	        if(s[i]==t[j]):
	            ans=self.get(s,t,i+1,j+1,dp)
	        else:
	            ans=min(self.get(s,t,i+1,j,dp),self.get(s,t,i,j+1,dp),self.get(s,t,i+1,j+1,dp))+1
	        dp[i][j]=ans
	    return dp[i][j]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends