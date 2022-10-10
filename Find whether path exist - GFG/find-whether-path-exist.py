
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if(grid[i][j]==1):
		            return self.get(grid,i,j)
		return False
	def get(self,grid,i,j):
	    if(i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0):
	        return False
	    elif(grid[i][j]==2):
	        return True
	    else:
	        grid[i][j]=0
	        return self.get(grid,i+1,j) or self.get(grid,i,j+1) or self.get(grid,i-1,j) or self.get(grid,i,j-1)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends