from bisect import bisect_left,bisect_right
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        arr=[]
        for i in range(len(s)):
            if(self.isPrime(s[i])):
                arr.append(i)
        if(len(arr)==0 or arr[0]!=0 or arr[-1]==len(s)-1):
            return 0
        self.mod=(10**9)+7
        arr.append(len(s))
        # print(arr)
        dp=[[-1 for __ in range(k+1)] for _ in range(len(arr))]
        return self.get(arr,0,dp,k,minLength)
    def get(self,arr,i,dp,k,minLength):
        # print(i,k,arr[i])
        if(i>=len(arr)-1):
            if(k!=0):
                return 0
            return 1
        elif(k==0):
            ans=1
            dp[i][k]=ans%self.mod
            return dp[i][k]
        elif(dp[i][k]!=-1):
            return dp[i][k]
        else:
            ans=0
            if(i==0):
                j=arr[i]
                r=bisect_left(arr,j+minLength)
                if(len(arr)==r):
                    dp[i][k]=0
                    return 0
                elif(arr[r]==arr[r-1]+1):
                    r=bisect_right(arr,arr[r]+1)
                    if(len(arr)==r):
                        dp[i][k]=0
                        return 0
                ans+=self.get(arr,r,dp,k-1,minLength)
            elif(arr[i-1]+1==arr[i]):
                ans=self.get(arr,i+1,dp,k,minLength)
            else:
                j=arr[i]
                r=bisect_left(arr,j+minLength)
                if(len(arr)==r):
                    dp[i][k]=0
                    return 0
                elif(arr[r]==arr[r-1]+1):
                    r=bisect_right(arr,arr[r]+1)
                    if(len(arr)==r):
                        dp[i][k]=0
                        return 0
                ans+=self.get(arr,r,dp,k-1,minLength)+self.get(arr,i+1,dp,k,minLength)
            dp[i][k]=(ans%self.mod)
            return dp[i][k]
    def isPrime(self,n):
        arr=["2","3","5","7"]
        if(n in arr):
            return True
        return False
                
            