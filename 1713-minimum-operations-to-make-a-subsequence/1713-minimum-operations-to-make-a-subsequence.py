from bisect import bisect_left
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d={}
        for i in range(len(target)):
            d[target[i]]=i
        a=[]
        for item in arr:
            if(item in d):
                a.append(d[item])
        ans=[]
        for item in a:
            if(len(ans)==0 or ans[-1]<item):
                ans.append(item)
            else:
                b=bisect_left(ans,item)
                ans[b]=item
        return len(target)-len(ans)