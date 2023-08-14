#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		xor=0
		for item in nums:
		    xor^=item
		num1=0
		num2=0
		for i in range(32):
		    if((xor>>i)&1==1):
		        for item in nums:
		            if((item>>i)&1==1):
		                num1^=item
		            else:
		                num2^=item
		        break
		return min(num1,num2),max(num1,num2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends