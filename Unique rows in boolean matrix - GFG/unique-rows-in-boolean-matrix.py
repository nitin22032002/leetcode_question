#User function Template for python3
class Solution:
    def uniqueRow(self,row, col, matrix):
        ans=[]
        r=set()
        for i in range(row):
            num=0
            for j in range(col):
                if(matrix[i][j]==1):
                    num|=(1<<j)
            if(num not in r):
                ans.append(matrix[i])
                r.add(num)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends