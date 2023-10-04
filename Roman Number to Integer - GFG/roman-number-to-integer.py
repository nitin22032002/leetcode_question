#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        for i in range(len(S)):
            if(i+1>=len(S) or d[S[i]]>=d[S[i+1]]):
                ans+=d[S[i]]
            else:
                ans-=d[S[i]]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends