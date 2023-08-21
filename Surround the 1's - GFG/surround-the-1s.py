#User function Template for python3

class Solution:
	def Count(self, matrix):
	    ans=0
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		        if(matrix[i][j]==0):continue
		        count=0
		        for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1],[i+1,j+1],[i-1,j-1],[i+1,j-1],[i-1,j+1]]:
		            if(i1<len(matrix) and j1<len(matrix[0]) and i1>=0 and j1>=0 and matrix[i1][j1]==0):
		                count+=1
		        if(count>0):
		            ans+=(1-(count%2))
		return ans    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends