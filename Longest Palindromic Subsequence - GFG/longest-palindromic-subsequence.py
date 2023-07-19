#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        return self.get(S,0,len(S)-1,{})
    def get(self,s,i,j,dp):
        if(i>j):
            return 0
        elif((i,j) in dp):return dp[(i,j)]
        else:
            if(s[i]==s[j]):
                ans=2+self.get(s,i+1,j-1,dp)
                if(i==j):ans-=1
            else:
                ans=max(self.get(s,i+1,j,dp),self.get(s,i,j-1,dp))
            dp[(i,j)]=ans
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends