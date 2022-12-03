#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        if(N==1):
            return S
        vowel={'a','e','i','o','u'}
        v=[]
        c=[]
        for item in S:
            if(item in vowel):
                v.append(item)
            else:
                c.append(item)
        v.sort()
        c.sort()
        if(abs(len(v)-len(c))>1):
            return -1
        start=True
        if(len(v)>len(c) or (len(v)==len(c) and v[0]<c[0])):
            start=False
        i=0
        j=0
        ans=[]
        while(i<len(v) or j<len(c)):
            if(start):
                ans.append(c[j])
                j+=1
            else:
                ans.append(v[i])
                i+=1
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