#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        d={0:1}
        s=0
        ans=0
        for item in S:
            if(item>='a' and item<='z'):
                s+=1
            else:
                s-=1
            if(s in d):
                ans+=d[s]
                d[s]+=1
            else:
                d[s]=1
        return ans

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends