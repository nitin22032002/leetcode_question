#User function Template for python3

class Solution:
    def isLucky(self, n): 
        start=2
        while(n>=start):
            if(n%start==0):return 0
            n=(n-(n//start))
            start+=1
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends