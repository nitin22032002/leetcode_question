#User function Template for python3

class Solution:
    def findNumber(self, N : int) -> int:
        val=[1,3,5,7,9]
        ans=[]
        mul=5
        pre=1
        while(N>0):
            r=(N%mul)-1
            r=(mul+r)%mul
            r//=pre
            ans.append(str(val[r]))
            N-=mul
            mul*=5
            pre*=5
        ans.reverse()
        ans="".join(ans)
        return int(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.findNumber(N)
        
        print(res)
        
# } Driver Code Ends