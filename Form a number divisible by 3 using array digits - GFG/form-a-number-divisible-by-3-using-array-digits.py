#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        x=0
        for item in arr:
            while(item!=0):
                x+=item%10
                item//=10
        return int(x%3==0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends