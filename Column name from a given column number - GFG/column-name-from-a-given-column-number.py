#User function Template for python3

class Solution:
    def colName (self, n):
        ans=[]
        while(n!=0):
            x=n%26
            if(x==0):
                ans.append("Z")
                n-=1
            else:
                ans.append(chr(64+x))
            n//=26
        return "".join(ans[::-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends