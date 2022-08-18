class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for item in arr:
            if(item not in d):
                d[item]=1
            else:
                d[item]+=1
        
        d=list(d.items())
        def key(val):
            return 1/(val[1])
        d.sort(key=key)
        # print(d)
        n=(len(arr))//2
        count=0
        ans=0
        for item in d:
            count+=item[1]
            ans+=1
            if(count>=n):
                break
        return ans
        