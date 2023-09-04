#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        for i in range(n):
            self.get(mat,i,0)
            self.get(mat,i,m-1)
        for i in range(m):
            self.get(mat,0,i)
            self.get(mat,n-1,i)
        for i in range(n):
            for j in range(m):
                if(mat[i][j]=="-1"):
                    mat[i][j]="O"
                elif(mat[i][j]=="O"):
                    mat[i][j]="X"
        return mat
    
    def get(self,mat,i,j):
        if(i>=len(mat) or i<0 or j>=len(mat[0]) or j<0 or mat[i][j]!="O"):
            return
        else:
            mat[i][j]="-1"
            for i1,j1 in [[i+1,j],[i,j-1],[i,j+1],[i-1,j]]:
                self.get(mat,i1,j1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends