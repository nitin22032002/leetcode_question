#User function Template for python3
from bisect import bisect_left
class Solution:
	def threeDivisors(self, query, q):
	    m=max(query)
	    dp=[False for _ in range(int(pow(m,0.5))+1)]
	    dp[0]=True
	    dp[1]=True
	    i=2
	    while(i*i<=m):
	        for j in range(i*i,len(dp),i):
	            dp[j]=True
	        i+=1
	    primes=[]
	    for i in range(len(dp)):
	        if(not dp[i]):
	            primes.append(i*i)
	    
        ans=[]
        for item in query:
            j=bisect_left(primes,item)
            if(j>=len(primes) or primes[j]>item):
                ans.append(j)
            else:
                ans.append(j+1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends