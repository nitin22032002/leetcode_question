class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        total=m*k
        if(len(arr)<total):
            return -1
        start=min(arr)
        end=max(arr)
        while(start<end):
            mid=(start+end)//2
            count=self.find(arr,mid,k)
            # print(count,mid,(start,end))
            if(count>=m):
                end=mid
            else:
                start=mid+1
        return start
    def find(self,arr,mid,k):
        i=0
        a=0
        ans=0
        while(i<len(arr)):
            if(a==k):
                ans+=1
                a=0
            if(arr[i]>mid):
                a=0
            else:
                a+=1
            i+=1
        if(a==k):
            ans+=1
        return ans
            