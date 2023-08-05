#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i=0
        j=M-1
        ans=1e9
        while(j<N):
            ans=min(ans,A[j]-A[i])
            i+=1
            j+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends