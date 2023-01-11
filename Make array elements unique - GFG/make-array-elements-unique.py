#User function Template for python3

class Solution:
    def minIncrements(self, arr, N): 
        arr.sort()
        # print(arr)
        val=0
        i=0
        ans=0
        while(i<N):
            # print(val,ans)
            if(val<arr[i]):
                val=arr[i]
            else:
                ans+=(val-arr[i]+1)
                val+=1
            i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr,N))
        
        T -= 1
# } Driver Code Ends