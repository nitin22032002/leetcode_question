#User function Template for python3

class Solution:
	def canPair(self, nums, k):
		
		d=[0 for _ in range(k)]
		for item in nums:
		    d[item%k]+=1
		i=1
		j=k-1
		while(i<j):
		    if(d[i]!=d[j]):
		        return False
		    i+=1
		    j-=1
		if(i==j):
		    if(d[i]%2!=0):
		        return False
	    return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends