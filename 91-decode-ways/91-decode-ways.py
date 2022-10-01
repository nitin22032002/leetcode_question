class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[-1 for _ in range(len(s))]
        return self.get(s,0,dp)
    def get(self,s,i,dp):
        if(i>=len(s)):
            return 1
        elif(dp[i]!=-1):
            return dp[i]
        elif(s[i]=="0"):
            dp[i]=0
            return 0
        else:
            if(i+1<len(s)):
                if(s[i+1]=="0" and int(s[i])<=2):
                    dp[i]=self.get(s,i+2,dp)
                else:
                    num=(int(s[i])*10+int(s[i+1]))
                    dp[i]=self.get(s,i+1,dp)
                    if(num<=26):
                        dp[i]+=self.get(s,i+2,dp)
            else:
                dp[i]=self.get(s,i+1,dp)
            return dp[i]