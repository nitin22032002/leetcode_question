class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        d=[[0,0,0] for _ in range(6)]
        for i in range(len(tops)):
            d[tops[i]-1][0]+=1
            d[bottoms[i]-1][1]+=1
            if(tops[i]==bottoms[i]):
                d[tops[i]-1][2]+=1
        ans=-1
        for i in range(6):
            a,b,c=d[i]
            if(a+b-c>=len(tops)):
                cost=(len(tops)-max(a,b))
                if(ans==-1):
                    ans=cost
                else:
                    ans=min(ans,cost)
        return ans