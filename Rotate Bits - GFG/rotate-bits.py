#User function Template for python3

class Solution:
    def rotate(self, N, D):
        D%=16
        left=(N>>D)|(N<<(16-D))&((1<<16)-1)
        right=((N<<D)|(N>>(16-D)))&((1<<16)-1)
        return [right,left]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends