#User function Template for python3

from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        d={}
        ans=0
        for i in range(n):
            val=gcd(numerator[i],denominator[i])
            p=(numerator[i]//val,denominator[i]//val)
            a,b=p
            p1=(b-a,b)
            if(p1 in d):
                ans+=d[p1]
            if(p in d):
                d[p]+=1
            else:
                d[p]=1
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends