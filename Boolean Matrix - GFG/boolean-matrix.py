#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    isRow=False
    isCol=False
    for i in range(len(matrix)):
        if(matrix[i][0]==1):
            isRow=True
            break
    for i in range(len(matrix[0])):
        if(matrix[0][i]==1):
            isCol=True
            break
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if(matrix[i][j]==1):
                matrix[i][0]=1
                matrix[0][j]=1
    for i in range(1,len(matrix)):
        if(matrix[i][0]==1):
            for j in range(1,len(matrix[0])):
                matrix[i][j]=1
    for i in range(1,len(matrix[0])):
        if(matrix[0][i]==1):
            for j in range(1,len(matrix)):
                matrix[j][i]=1
    if(isRow):
        for i in range(len(matrix)):
            matrix[i][0]=1
    if(isCol):
        for i in range(len(matrix[0])):
            matrix[0][i]=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends