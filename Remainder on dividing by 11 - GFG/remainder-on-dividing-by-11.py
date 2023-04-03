#User function Template for python3


class Solution:
    def xmod11(self,x):
        ans=0
        for i in range(len(x)):
            ans*=(10)
            ans+=(int(x[i]))
            ans%=11
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        x = input()
        
        ob = Solution()
        
        print(ob.xmod11(x))

# } Driver Code Ends