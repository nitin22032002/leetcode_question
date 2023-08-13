
class Solution:
    def nthFibonacci(self, n : int) -> int:
        prv=0
        next=1
        mod=int(1e9+7)
        while(n!=0):
            t=(prv+next)%mod
            prv=next
            next=t
            n-=1
        return prv
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends