#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        ans=0
        i=0
        while(i<n):
            c=0
            while(i<n and arr[i]==0):
                i+=1
                c+=1
            ans+=((c)*(c+1))//2
            while(i<n and arr[i]==1):
                i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends