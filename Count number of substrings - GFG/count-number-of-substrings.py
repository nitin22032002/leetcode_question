#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        return self.findAtmost(s,k)-self.findAtmost(s,k-1)
    
    def findAtmost(self,s,k):
        d={}
        ans=i=j=0
        while(j<len(s)):
            if(len(d)<=k):
                ans+=(j-i)
                d[s[j]]=j
                j+=1
            else:
                if(d[s[i]]==i):
                    del d[s[i]]
                i+=1
        while(i<len(s) and len(d)>k):
            if(d[s[i]]==i):
                del d[s[i]]
            i+=1
        ans+=(j-i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends