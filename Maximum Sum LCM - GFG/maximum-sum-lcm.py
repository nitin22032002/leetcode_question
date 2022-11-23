#User function Template for python3
class Solution:
    def maxSumLCM (self, n):
        i=self.isPrime(n)
        return i
            
    def isPrime(self,n):
        i=1
        ans=0
        while(i*i<=n):
            if(n%i==0):
                if(i==(n//i)):
                    ans+=i
                else:
                    ans+=(i+(n//i))
            i+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends