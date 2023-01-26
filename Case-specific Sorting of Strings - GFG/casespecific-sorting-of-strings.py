#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        upper=[0 for _ in range(26)]
        lower=[0 for _ in range(26)]
        for i in range(n):
            if(s[i]>='a' and s[i]<='z'):
                lower[ord(s[i])-97]+=1
            else:
                upper[ord(s[i])-65]+=1
        i=0
        j=0
        k=0
        # print(lower,upper)
        ans=[]
        while(i<len(s)):
            if(s[i]>='a' and s[i]<='z'):
                if(lower[j]==0):
                    j+=1
                    continue
                else:
                    ans.append(chr(j+97))
                    lower[j]-=1
                    i+=1
            else:
                if(upper[k]==0):
                    k+=1
                    continue
                else:
                    ans.append(chr(k+65))
                    upper[k]-=1
                    i+=1
        return "".join(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends