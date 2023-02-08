#User function Template for python3
class Solution():
    def countZero(self, n, k ,arr):
        total=(n*n)
        row=set()
        col=set()
        ans=[]
        for a,b in arr:
            if(a not in row):
                total-=(n-len(col))
                row.add(a)
            if(b not in col):
                total-=(n-len(row))
                col.add(b)
            ans.append(total)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends