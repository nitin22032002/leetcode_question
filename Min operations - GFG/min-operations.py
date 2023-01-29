class Solution:
    def solve(self, a : int, b : int) -> int:
        isDone1=0
        isDone2=0
        for i in range(0,32):
            b1=(a>>i)&1
            b2=(b>>i)&1
            if(b1!=b2):
                if(b1==1):
                    isDone1=1
                elif(b2==1):
                    isDone2=1
        return isDone1+isDone2
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends