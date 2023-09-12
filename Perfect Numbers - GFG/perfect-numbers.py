#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        ans=0
        i=1
        while(i*i<=N):
            if(N%i==0):
                ans+=i
                if((N//i)!=i):
                    ans+=(N//i)
            i+=1
        return int(ans-N==N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends