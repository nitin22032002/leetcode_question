#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        if(N==1):
            return S
        vowel={'a','e','i','o','u'}
        v=[0 for _ in range(26)]
        c=[0 for _ in range(26)]
        r1=0
        for item in S:
            j=ord(item)-97
            if(item in vowel):
                v[j]+=1
                r1+=1
            else:
                c[j]+=1
        r2=N-r1
        if(abs(r1-r2)>1):
            return -1
        i=0
        j=0
        while(i<len(v) and v[i]==0):
            i+=1
        while(j<len(c) and c[j]==0):
            j+=1
        start=True
        if(r1>r2 or (r1==r2 and i<j)):
            start=False
        ans=[]
        while(i<len(v) or j<len(c)):
            if(start and j<len(c)):
                if(c[j]==0):
                    j+=1
                    continue
                ans.append(chr(j+97))
                c[j]-=1
            elif(not start and i<len(v)):
                if(v[i]==0):
                    i+=1
                    continue
                ans.append(chr(i+97))
                v[i]-=1
            start=not start
        return "".join(ans)
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends