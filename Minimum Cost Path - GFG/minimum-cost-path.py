from queue import PriorityQueue
class Solution:
	def minimumCostPath(self, grid):
	    obj=PriorityQueue()
	    visited=[[-1 for _ in range(len(grid[0]))] for __ in range(len(grid))]
	    obj.put([grid[0][0],0,0])
	    visited[0][0]=grid[0][0]
	    while(not obj.empty()):
	        cost,i,j=obj.get()
	        if(i==len(grid)-1 and j==len(grid[0])-1):
	            return cost
	        else:
	            for i1,j1 in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
	                if(i1>=0 and i1<len(grid) and j1>=0 and j1<len(grid[0])):
	                    if(visited[i1][j1]==-1 or visited[i1][j1]>grid[i1][j1]+cost):
	                        visited[i1][j1]=grid[i1][j1]+cost
	                        obj.put([visited[i1][j1],i1,j1])
	        
	    return -1


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
		ans = obj.minimumCostPath(grid)
		print(ans)

# } Driver Code Ends