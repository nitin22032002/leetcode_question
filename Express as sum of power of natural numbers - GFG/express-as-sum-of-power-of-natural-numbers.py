#User function Template for python3
class Solution:
	def numOfWays(self, n, x):
	    arr=[]
	    i=1
	    while(n>=pow(i,x)):
	        arr.append(pow(i,x))
	        i+=1
	    dp=[[-1 for _ in range(len(arr))] for __ in range(n+1)]
	    return self.get(arr,0,dp,n)
	def get(self,arr,i,dp,s):
	    if(s==0):
	        return 1
	    elif(i>=len(arr) or s<0):
	        return 0
        elif(dp[s][i]!=-1):
            return dp[s][i]
        else:
            ans=self.get(arr,i+1,dp,s)+self.get(arr,i+1,dp,s-arr[i])
            ans%=int(1e9+7)
            dp[s][i]=ans
            return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,x = input().split()
		n=int(n)
		x=int(x)
		ob = Solution();
		print(ob.numOfWays(n, x))

# } Driver Code Ends