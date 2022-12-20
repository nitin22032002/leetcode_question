class Solution:
    def maxDistance (self, arr, n) : 
        m1_min=arr[0]
        m1_max=arr[0]
        m2_min=arr[0]
        m2_max=arr[0]
        for i in range(n):
            m1_min=min(m1_min,arr[i]+i)
            m1_max=max(m1_max,arr[i]+i)
            m2_min=min(m2_min,arr[i]-i)
            m2_max=max(m2_max,arr[i]-i)
        return max(m1_max-m1_min,m2_max-m2_min)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().maxDistance(arr, n)
    print(ans)
    





# } Driver Code Ends