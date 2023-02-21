#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        ans=0
        for i in range(N):
            for j in range(M):
                r=abs(x-1-i)+abs(y-1-j)
                ans=max(ans,r)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends