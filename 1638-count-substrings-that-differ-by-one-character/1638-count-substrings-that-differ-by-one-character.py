class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        dp=[[-1 for _ in range(len(t))] for __ in range(len(s))]
        ans=self.get(s,t,0,0,dp)
        return ans
    def get(self,s,t,i,j,dp):
        if(i>=len(s) or j>=len(t)):
            return 0
        elif(dp[i][j]!=-1):
            return 0
        else:
            dp[i][j]=0
            if(s[i]!=t[j]):
                right=0
                a1=i+1
                t1=j+1
                while(a1<len(s) and t1<len(t) and s[a1]==t[t1]):
                    right+=1
                    a1+=1
                    t1+=1
                a1=i-1
                left=0
                t1=j-1
                while(a1>=0 and t1>=0 and s[a1]==t[t1]):
                    left+=1
                    a1-=1
                    t1-=1
                l=(left*right+left+right+1)
                # print((i,j),l)
                dp[i][j]+=l
            dp[i][j]+=(self.get(s,t,i,j+1,dp)+self.get(s,t,i+1,j,dp))
            return dp[i][j]