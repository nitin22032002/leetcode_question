#User function Template for python3


class Solution:
    def waysToBreakNumber(self, n):
        ans=((n+1)*(n+2))//2
        ans%=((10**9)+7)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        print(ob.waysToBreakNumber(n))
        
# } Driver Code Ends