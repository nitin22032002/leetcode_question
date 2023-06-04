#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        ans=[]
        i=len(s)-1
        while(i>=0):
            val=""
            while(i>=0 and s[i]>='0' and s[i]<='9'):
                val+=s[i]
                i-=1
            if(val!=""):
                ans.append(val[::-1])
            if(i>=0):
                ans.append(s[i])
                i-=1
        return "".join(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends