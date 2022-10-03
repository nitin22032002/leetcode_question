class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=0
        ans=0
        while(i<len(colors)):
            j=i
            cost=0
            m=0
            while(j<len(colors) and colors[i]==colors[j]):
                m=max(m,neededTime[j])
                cost+=neededTime[j]
                j+=1
            ans+=(cost-m)
            i=j
        return ans