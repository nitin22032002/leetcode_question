#User function Template for python3
class Solution:
	def reverseSpiral(self, m, n, matrix):
		ans=[]
        i=0
        while(len(ans)<m*n):
            j=i
            k=i
            while(j<n-i):
                ans.append(matrix[k][j])
                j+=1
            # print(ans)
            j-=1
            k+=1
            if(k<m-i):
                while(k<m-i):
                    ans.append(matrix[k][j])
                    k+=1
                # print(ans)
                k-=1
                j-=1
                while(j>=i):
                    ans.append(matrix[k][j])
                    j-=1
                
                j+=1
                k-=1
                while(k>i and j!=n-i-1):
                    ans.append(matrix[k][j])
                    k-=1
            i+=1
        return ans[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends