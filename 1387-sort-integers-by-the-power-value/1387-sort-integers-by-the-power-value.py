class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l=[i for i in range(lo,hi+1)]
        l.sort(key=self.power)
        return l[k-1]
    def power(self,n):
        if(n==1):
            return 0
        elif(n%2==0):
            return 1+self.power(n//2)
        else:
            return 1+self.power(3*n+1)