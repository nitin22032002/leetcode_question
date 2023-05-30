class Solution:
	def isWordExist(self, board, word):
	    for i in range(len(board)):
	        for j in range(len(board[0])):
	            s=self.get(board,i,j,0,word)
	            if(s):
	               # print(i,j)
	                return True
	    return False
	   #return self.get(board,1,0,0,word)
    def get(self,board,i,j,k,word):
        if(k>=len(word)):
            # print(i,j)
            return True
        elif(i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]=="-1"):
            return False
        elif(word[k]!=board[i][j]):
            return False
        else:
            # print((i,j))
            board[i][j]="-1"
            status=False
            for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                status=status or self.get(board,i1,j1,k+1,word)
            board[i][j]=word[k]
            return status

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends