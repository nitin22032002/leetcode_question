#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        d={}
        i=j=0
        ans=-1
        while(j<len(s)):
            if(len(d)==k):
                ans=max(ans,j-i)
            if(len(d)>k):
                d[s[i]]-=1
                if(d[s[i]]==0):
                    del d[s[i]]
                i+=1
            else:
                if(s[j] in d):
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                j+=1
        if(len(d)==k):
            ans=max(ans,j-i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends