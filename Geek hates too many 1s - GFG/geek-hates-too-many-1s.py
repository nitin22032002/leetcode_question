class Solution:
    def noConseBits(self, n : int) -> int:
        c=0
        for i in range(31,-1,-1):
            if((n>>i)&1!=0):
                c+=1
                if(c==3):
                    n^=(1<<i)
                    c=0
            else:
                c=0
        return n
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends