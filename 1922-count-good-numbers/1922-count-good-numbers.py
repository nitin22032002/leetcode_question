class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime=4
        even=5
        mid=n//2
        mod=((10**9)+7)
        if(n%2==0):
            x=pow(even,mid,mod)
        else:
            x=pow(even,mid+1,mod)
        ans=(x*pow(prime,mid,mod))%(mod)
        return ans