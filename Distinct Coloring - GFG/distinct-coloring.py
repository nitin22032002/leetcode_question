#User function Template for python3

class Solution:
    def distinctColoring (self, N, r, g, b):
        red,green,blue=r[0],g[0],b[0]
        for i in range(1,N):
            red,green,blue=min(green,blue)+r[i],min(red,blue)+g[i],min(red,green)+b[i]
        return min(red,green,blue) 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        r = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
# } Driver Code Ends