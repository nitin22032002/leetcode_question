class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        start=1
        end=pow(2,n-1)
        return self.get(start,end,False,k)
    def get(self,start,end,target,k):
        mid=(start+end)//2
        if(start==end):
            if(target):
                return 1
            return 0
        if(k<=mid):
            return self.get(start,mid,target,k)
        else:
            return self.get(mid+1,end,not target,k)