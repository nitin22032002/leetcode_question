#User function Template for python3
from bisect import bisect_right
class Solution:
    def median(self, matrix, R, C):
    	start=1
    	end=2000
    	tr=(R*C+1)//2
    	while(start<end):
    	    mid=(start+end)//2
    	    m=self.findHow(matrix,mid)
    	    if(m>=tr):
    	        end=mid
    	    else:
    	        start=mid+1
        return start
    def findHow(self,matrix,target):
        ans=0
        for item in matrix:
            ans+=bisect_right(item,target)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends