#User function Template for python3
from math import gcd
class Solution:
    def minimumSquares(self, L, B):
        tem=gcd(L,B)
        return [(L//tem)*(B//tem),tem]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends