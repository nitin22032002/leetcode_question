class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[-1 for _ in range(len(s))]
        return self.get(s,0,dp)
    def get(self,s,i,dp):
        if(i>=len(s)):
            return 1
        elif(s[i]=="0"):
            return 0
        elif(dp[i]!=-1):
            return dp[i]
        elif(s[i]=="*"):
            ans=(9*self.get(s,i+1,dp))
            if(i+1<len(s)):
                if(s[i+1]!="*"):
                    if(int(s[i+1])<=6):
                        ans+=self.get(s,i+2,dp)*2
                    else:
                        ans+=self.get(s,i+2,dp)
                else:
                    ans+=(15*self.get(s,i+2,dp))
            dp[i]=(ans)%((10**9)+7)
            return dp[i]
        else:
            ans=self.get(s,i+1,dp)
            if(i+1<len(s)):
                if(s[i+1]!="*"):
                    num=int(s[i:i+2])
                    if(num<=26):
                        ans+=self.get(s,i+2,dp)
                else:
                    if(s[i]=="1"):
                        ans+=(9*self.get(s,i+2,dp))
                    elif(s[i]=="2"):
                        ans+=(6*self.get(s,i+2,dp))
            dp[i]=(ans)%((10**9)+7)
            return dp[i]
                