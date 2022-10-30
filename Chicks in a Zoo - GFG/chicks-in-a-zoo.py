#User function Template for python3

class Solution:
	def NoOfChicks(self, N):
		s=1
		p=1
		arr=[1]
		for i in range(2,N+1):
		    arr.append(s*2)
		  #  print(s)
		    s=s*3
		    if(i>=6):
		      #  print(i-6)
		        s-=arr[i-6]
# 		print(arr)
        if(N>=6):
            s+=arr[N-6]
		return s    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		obj = Solution()
		ans = obj.NoOfChicks(N)
		print(ans)

# } Driver Code Ends