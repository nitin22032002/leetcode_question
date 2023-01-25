#User function Template for python3

class Solution:
    def minOperation(self, s): 
        ans=len(s)
        for i in range(len(s)//2):
            k=0
            j=i+1
            while(k<=i):
                if(s[k]!=s[j]):break
                k+=1
                j+=1
            else:
                # print(i)
                ans=min(ans,i+2+len(s)-2*(i+1))
        return ans
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
# } Driver Code Ends