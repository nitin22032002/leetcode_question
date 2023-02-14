#User function Template for python3

class Solution():
    def minCost(self, colors, N):
        a=b=c=0
        for i in range(N):
            a,b,c=min(b,c)+colors[i][0],min(a,c)+colors[i][1],min(a,b)+colors[i][2]
        return min(a,b,c)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ =="__main__":
    for _ in range(int(input())):
        n = int(input())
        colors = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            colors.append(tmp)
        print(Solution().minCost(colors, n))
# } Driver Code Ends