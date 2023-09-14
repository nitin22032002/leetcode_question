#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
	    return self.get(arr,sum,0,{})
    def get(self,arr,s,i,dp):
        if(i>=len(arr) or s<0):
            if(s==0):return 1
            return 0
        elif((i,s) in dp):
            return dp[(i,s)]
        else:
            ans=self.get(arr,s,i+1,dp)+self.get(arr,s-arr[i],i+1,dp)
            ans%=(int(1e9+7))
            dp[(i,s)]=ans
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends