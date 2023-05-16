#User function Template for python3
class Solution:
    def cuts(self, s):
        dp=[-1]*len(s)
        ans=self.get(s,0,dp)
        if(ans>=1e9):return -1
        return ans
    def get(self,s,i,dp):
        if(i>=len(s)):
            return 0
        elif(dp[i]!=-1):
            return dp[i]
        elif(s[i]=='0'):
            dp[i]= 1e9
        else:
            res=0
            ans=1e9
            for j in range(i,len(s)):
                res*=2
                if(s[j]=='1'):
                    res+=1
                if(self.isPower(res,5)):
                    ans=min(ans,self.get(s,j+1,dp)+1)
            dp[i]=ans
        return dp[i]
    
    def isPower(self,n,p):
        while(n%p==0):
            n//=p
        return (n==1)
                    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.cuts(s))

# } Driver Code Ends