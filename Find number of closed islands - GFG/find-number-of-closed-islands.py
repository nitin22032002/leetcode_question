#User function Template for python3

class Solution:
	def closedIslands(self, matrix, N, M):
	    ans=0
	    for i in range(N):
	        for j in range(M):
	            if(matrix[i][j]==1):
	                if(self.get(matrix,i,j)):
	                    ans+=1
	    return ans
	def get(self,mat,i,j):
	    if(i>=len(mat) or i<0 or j>=len(mat[0]) or j<0):return False
	    elif(mat[i][j]==0):return True
	    else:
	        mat[i][j]=0
	        return all([self.get(mat,i+1,j),self.get(mat,i-1,j),self.get(mat,i,j+1),self.get(mat,i,j-1)])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends