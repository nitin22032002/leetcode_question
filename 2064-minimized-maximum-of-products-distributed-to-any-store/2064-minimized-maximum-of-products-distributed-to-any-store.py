from math import ceil
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        s=sum(quantities)
        start=ceil(s/n)
        end=max(quantities)
        while(end>start):
            mid=(start+end)//2
            x=self.shops(quantities,mid)
            # print(mid,x)
            if(x>n):
                start=mid+1
            else:
                end=mid
        return start
    def shops(self,arr,m):
        ans=0
        for item in arr:
            ans+=(ceil(item/m))
        return ans