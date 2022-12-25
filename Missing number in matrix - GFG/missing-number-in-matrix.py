#User function Template for python3

class Solution:
	def MissingNo(self, matrix):
	    nonZero=-1
	    zero=-1
	    for i in range(len(matrix)):
	        s=0
	        isZero=False
	        for j in range(len(matrix[0])):
	            s+=matrix[i][j]
	            if(matrix[i][j]==0):
	                isZero=True
	        if(isZero):
	            if(zero==-1):
	                zero=s
	            elif(zero!=s):
	                return -1
	        else:
	            if(nonZero==-1):
                    nonZero=s
                elif(nonZero!=s):return -1
        for j in range(len(matrix[0])):
	        s=0
	        isZero=False
	        for i in range(len(matrix)):
	            s+=matrix[i][j]
	            if(matrix[i][j]==0):
	                isZero=True
	        if(isZero):
	            if(zero==-1):
	                zero=s
	            elif(zero!=s):
	                return -1
	        else:
	            if(nonZero==-1):
                    nonZero=s
                elif(nonZero!=s):return -1
        s=0
	    isZero=False
	    for i in range(len(matrix)):
	        s+=matrix[i][i]
	        if(matrix[i][i]==0):
	                isZero=True
	    if(isZero):
	       if(zero==-1):
	           zero=s
	       elif(zero!=s):
	           return -1
	    else:
	        if(nonZero==-1):
	            nonZero=s
            elif(nonZero!=s):return -1
        s=0
	    isZero=False
	    for i in range(len(matrix)):
	        s+=matrix[i][len(matrix)-i-1]
	        if(matrix[i][len(matrix)-i-1]==0):
	                isZero=True
	    if(isZero):
	       if(zero==-1):
	           zero=s
	       elif(zero!=s):
	           return -1
	    else:
	        if(nonZero==-1):
	            nonZero=s
            elif(nonZero!=s):return -1
        if(zero>=nonZero):
            return -1
        return nonZero-zero
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.MissingNo(matrix)
		print(ans)

# } Driver Code Ends