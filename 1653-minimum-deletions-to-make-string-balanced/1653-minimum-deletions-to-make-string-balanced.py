class Solution:
    def minimumDeletions(self, s: str) -> int:
        d=[[-1,-1] for _ in range(len(s))]
        return self.get(s,0,0,d)
    def get(self,s,i,state,d):
        if(i>=len(s)):
            return 0
        elif(d[i][state]!=-1):
            return d[i][state]
        else:
            j=ord(s[i])-97
            if(state==0):
                ans=min(self.get(s,i+1,j,d),1+self.get(s,i+1,state,d))
            else:
                if(j==1):
                    ans=self.get(s,i+1,state,d)
                else:
                    ans=1+self.get(s,i+1,state,d)
            d[i][state]=ans
            return ans