#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, S): 
        d={}
        for item in S:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        i=0
        j=len(S)-1
        front=[""]
        back=[""]
        c=0
        while(i<=j):
            if(c%2==0):
                if(d[S[i]]>1):
                    d[S[i]]-=1
                    i+=1
                    c+=1
                else:
                    front.append(S[i])
                    i+=1
            else:
                if(d[S[j]]>1):
                    d[S[j]]-=1
                    j-=1
                    c+=1
                else:
                    back.append(S[j])
                    j-=1
        if(c%2==0):
            return "".join(front)+"".join(back[::-1])
        else:
            return "".join(back)+"".join(front[::-1])

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends