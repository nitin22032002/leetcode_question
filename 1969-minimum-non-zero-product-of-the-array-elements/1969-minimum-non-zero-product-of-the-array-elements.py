class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n=pow(2,p)
        int_max=(10**9)+7
        mid=(n-2)//2
        ans=pow(n-2,mid,int_max)*((n-1)%int_max)
        return ans%int_max