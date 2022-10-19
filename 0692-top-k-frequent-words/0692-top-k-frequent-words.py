class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for item in words:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        d=list(d.items())
        d.sort(key=lambda x:[-x[1],x[0]])
        ans=[]
        for i in range(k):
            ans.append(d[i][0])
        return ans