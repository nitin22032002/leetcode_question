#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        i=0
        j=0
        c=0
        ans=0
        while(j<n):
            if(c<=m):
                ans=max(ans,j-i)
                if(arr[j]=='O'):
                    c+=1
                j+=1
            else:
                if(arr[i]=='O'):
                    c-=1
                i+=1
        while(i<n and c>m):
            if(arr[i]=='O'):
                c-=1
            i+=1
        ans=max(ans,j-i)
        return ans 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends