#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        ans=0
        sign=1
        if(s1[0]=="-"):
            s1=s1[1:]
            sign*=-1
        if(s2[0]=="-"):
            s2=s2[1:]
            sign*=-1
        p=1
        for i in s1[::-1]:
            r=p
            for j in s2[::-1]:
                ans+=(int(i)*int(j)*r)
                r*=10
            p*=10
        return ans*sign


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends