#User function Template for python3

class Solution():
    def modulo(self, s, m):
        ans=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='1'):
                ans+=pow(2,len(s)-i-1,m)
                ans%=m
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends