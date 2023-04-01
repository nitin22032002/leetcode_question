#User function Template for python3

class Solution:
    def minOperations(self, N):
        r=N//2
        s1=(r*(1+(2*(r-1)+1)))//2
        if(N%2==0):
            s2=(r*(2*(r)+1+(2*(N-1)+1)))//2
        else:
            s2=(r*(2*(r+1)+1+(2*(N-1)+1)))//2
        return (s2-s1)//2
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends