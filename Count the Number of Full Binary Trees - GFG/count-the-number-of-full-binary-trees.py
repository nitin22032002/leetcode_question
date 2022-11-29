#User function Template for python3

class Solution:
    def numoffbt(self, arr, n):
        if(n<=2):
            return n
        mod=(10**9)+7
        maxVal=max(arr)
        mp=[0 for _ in range(maxVal+1)]
        dp=[0 for _ in range(maxVal+1)]
        for item in arr:
            mp[item]=1
            dp[item]=1
        for i in range(maxVal+1):
            if(mp[i]==1):
                j=2*i
                while(j<=maxVal and (j//i)<=i):
                    if(j%i==0 and mp[j]==1):
                        mul=2
                        if((j//i)==i):
                            mul=1
                        dp[j]+=(mul*dp[i]*dp[j//i])
                        dp[j]%=mod
                    j+=i
        ans=sum(dp)
        ans%=mod
        # print(dp)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.numoffbt(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends