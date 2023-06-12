#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        dp=[0 for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i):
                dp[i]=max(dp[i-(j+1)]+price[j],dp[i])
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends