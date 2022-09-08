from bisect import bisect_left,insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(1,m):
                matrix[i][j]+=matrix[i][j-1]
        ans=-10**8
        # print(matrix)
        for col1 in range(m):
            for col2 in range(col1,m):
                s=0
                arr=[0]
                for row in range(n):
                    s+=self.getSum(matrix,row,col1,col2)
                    diff=s-k
                    ind=bisect_left(arr,diff)
                    if(ind<len(arr)):
                        if(arr[ind]==diff):
                            return k
                        else:
                            ans=max(ans,s-arr[ind])
                    insort(arr,s)
        return ans
    
    def getSum(self,matrix,row,col1,col2):
        if(col1==0):
            return matrix[row][col2]
        else:
            return (matrix[row][col2]-matrix[row][col1-1])
        