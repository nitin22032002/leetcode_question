from bisect import bisect_left
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibb=[1]
        start=2
        while(start<=k):
            fibb.append(start)
            start=fibb[-2]+start
        ans=0
        while(k!=0):
            a=bisect_left(fibb,k)
            if(a<len(fibb) and fibb[a]==k):
                ans+=1
                break
            else:
                k-=fibb[a-1]
                ans+=1
        return ans