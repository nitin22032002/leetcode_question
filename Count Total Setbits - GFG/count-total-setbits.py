

class Solution:
    def countBits(self, N : int) -> int:
        ans=0
        for i in range(32):
            x=1<<i
            ans+=((N+1)//(2*x))*x
            r=((N+1)%(x*2))-x
            ans+=max(r,0)
        return ans
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.countBits(N)
        
        print(res)
        

# } Driver Code Ends