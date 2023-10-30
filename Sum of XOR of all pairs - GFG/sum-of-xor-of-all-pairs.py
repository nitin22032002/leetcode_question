#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        ans=0
        bits=[0 for _ in range(32)]
        for item in arr:
            for i in range(32):
                bits[i]+=((item>>i)&1)
        for i in range(len(bits)):
            x=bits[i]*(n-bits[i])
            ans+=((1<<i)*x)
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends