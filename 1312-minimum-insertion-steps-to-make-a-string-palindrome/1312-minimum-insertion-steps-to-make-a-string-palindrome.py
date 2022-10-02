class Solution:
    def minInsertions(self, s: str) -> int:
        return self.get(s,0,len(s)-1,{})
    def get(self,s,i,j,dp):
        if(i>=j):
            return 0
        elif((i,j) in dp):
            return dp[(i,j)]
        else:
            if(s[i]==s[j]):
                dp[(i,j)]=self.get(s,i+1,j-1,dp)
            else:
                dp[(i,j)]=min(self.get(s,i+1,j,dp),self.get(s,i,j-1,dp))+1
            return dp[(i,j)]