class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans=0
        for i in range(len(rating)):
            l1=0
            g1=0
            for j in range(0,i):
                if(rating[j]<rating[i]):
                    l1+=1
                else:
                    g1+=1
            l2=0
            g2=0
            for j in range(i+1,len(rating)):
                if(rating[j]<rating[i]):
                    l2+=1
                else:
                    g2+=1
            ans+=(l1*g2)
            ans+=(l2*g1)
        return ans
            