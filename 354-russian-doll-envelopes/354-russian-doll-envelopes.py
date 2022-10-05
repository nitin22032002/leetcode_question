from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def key(val):
            return [val[0],-val[1]]
        envelopes.sort(key=key)
        a1=self.LIS(envelopes)
        return a1
    def LIS(self,arr):
        ans=[]
        for item in arr:
            if(len(ans)==0 or ans[-1]<item[1]):
                ans.append(item[1])
            else:
                f=bisect_left(ans,item[1])
                ans[f]=item[1]
        return len(ans)