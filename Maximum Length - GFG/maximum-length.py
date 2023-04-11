#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        r=a+b+c
        a1,b1,c1=sorted([a,b,c],reverse=True)
        t1=(2*c1)+1
        t2=(b1-c1)
        if(a1>=(t1+t2)*2):return -1
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends