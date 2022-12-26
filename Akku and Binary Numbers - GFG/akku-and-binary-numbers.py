#User function Template for python3
from bisect import bisect_left,bisect_right
class Solution:
    dp=[]
    def solve (self, L, R):
        i=bisect_left(self.dp,L)
        j=bisect_right(self.dp,R)
        ans=j-i
        return ans
    def precompute (self):
        for i in range(64):
            for j in range(i+1,64):
                for k in range(j+1,64):
                    b1=1<<i
                    b2=1<<j
                    b3=1<<k
                    self.dp.append(b1|b2|b3)
        self.dp.sort()
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends