#User function Template for python3

from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        d={}
        for i in range(n):
            val=gcd(numerator[i],denominator[i])
            p=(numerator[i]//val,denominator[i]//val)
            if(p in d):
                d[p]+=1
            else:
                d[p]=1
        ans=0
        for item in d:
            a,b=item
            p1=(b-a,b)
            if(p1 in d):
                val=d[p1]
                if(p1==item):
                    ans+=(val*(val-1))
                elif(p1!=item):
                    ans+=(val*(d[item]))
        return ans//2


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