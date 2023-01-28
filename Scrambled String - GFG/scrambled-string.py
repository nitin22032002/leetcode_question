#User function Template for python3

class Solution:
    def isScramble(self,S1: str, S2: str):
        ans=self.get(S1,S2,0,0,len(S1),{})
        return ans
    def get(self,s1,s2,start1,start2,n,dp):
        # print((start1,start2,n))
        if(n==1):
            return (s1[start1]==s2[start2])
        elif((start1,start2,n) in dp):
            return dp[(start1,start2,n)]
        else:
            status=True
            for i in range(1,n):
                a=self.get(s1,s2,start1,start2,i,dp) and self.get(s1,s2,start1+i,start2+i,n-i,dp)
                if(a):break
                a=self.get(s1,s2,start1,start2+n-i,i,dp) and self.get(s1,s2,start1+i,start2,n-i,dp)
                if(a):break
            else:
                status=False
            dp[(start1,start2,n)]=status
            return status
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        S1,S2=input().split()
        if(Solution().isScramble( S1 , S2)):
            print("Yes")
        
        else:
            print("No")


# } Driver Code Ends