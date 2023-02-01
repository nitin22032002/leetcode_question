#User function Template for python3

class Solution:
    def distinctColoring (self, N, r, g, b):
        red=r[0]
        green=g[0]
        blue=b[0]
        for i in range(1,N):
            a1=min(green,blue)+r[i]
            a2=min(red,blue)+g[i]
            a3=min(red,green)+b[i]
            red,green,blue=a1,a2,a3
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