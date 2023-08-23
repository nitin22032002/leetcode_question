#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		ans=[]
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if(self.get(grid,word,i,j)):
		            ans.append([i,j])
		return ans
	
	def get(self,grid,word,i,j):
	    i1=i
	    j1=j
	    for a,b in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
    	    k=0
    	    i=i1
    	    j=j1
    	    while(k<len(word) and i<len(grid) and j<len(grid[0]) and i>=0 and j>=0):
    	        if(grid[i][j]!=word[k]):
    	            break
    	        i+=a
    	        j+=b
    	        k+=1
    	    if(k==len(word)):
    	        return True
	    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends