#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		return self.get(str,0,0,{})
	def get(self,str,i,j,dp):
	    if(i>=len(str) or j>=len(str)):
	        return 0
	    elif((i,j) in dp):
	        return dp[(i,j)]
	    else:
	        if(i==j):
	            ans=self.get(str,i,j+1,dp)
	        elif(str[i]==str[j]):
	            ans=1+self.get(str,i+1,j+1,dp)
	        else:
	            ans=max(self.get(str,i+1,j,dp),self.get(str,i,j+1,dp),self.get(str,i+1,j+1,dp))
	        dp[(i,j)]=ans
	        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends