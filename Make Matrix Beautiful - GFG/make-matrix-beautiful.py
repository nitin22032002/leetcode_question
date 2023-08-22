#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        row=[0 for _ in range(n)]
        col=[0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                row[i]+=matrix[i][j]
                col[j]+=matrix[i][j]
        target=max(row+col)
        ans=0
        for i in range(n):
            for j in range(n):
                r=max(row[i],col[j])
                if(r<target):
                    x=(target-r)
                    ans+=x
                    row[i]+=x
                    col[j]+=x
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends