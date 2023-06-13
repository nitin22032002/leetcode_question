#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        for i in range(n):
            arr[i]+=k
        ans=arr[-1]-arr[0]
        mi=arr[0]

        mr=arr[-1]
        j=n-1
        while(j>=0 and arr[j]-2*k>=0):
            arr[j]-=2*k
            mr=max(arr[-1],arr[j])
            if(j-1>=0):
                mr=max(mr,arr[j-1])
            mi=min(mi,arr[j])
            ans=min(ans,mr-mi)
            j-=1
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends