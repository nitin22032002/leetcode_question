#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        i=0
        j=0
        r=0
        ans=-1
        while(r<len(A)):
            i=r
            j=0
            while(i<len(A) and j<len(B)):
                if(A[i]!=B[j]):
                    break
                i+=1
                j+=1
            else:
                ans=self.get(A,B,j)
                if(ans!=-1):
                    return ans+1
            r+=1
        return -1
    def get(self,A,B,j):
        ans=0
        while(j<len(B)):
            i=0
            while(j<len(B) and i<len(A)):
                if(A[i]!=B[j]):
                    return -1
                i+=1
                j+=1
            else:
                ans+=1
        return ans
                
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends