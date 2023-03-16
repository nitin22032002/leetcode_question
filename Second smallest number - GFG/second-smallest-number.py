#User function Template for python3

class Solution:
    def secondSmallest(self, S, D):
        if(D*9<S):
            return "-1"
        ans=[9]*D
        curr=9*D
        i=0
        while(curr>S and i<D):
            f=curr-S
            ans[i]-=min(f,8+min(i,1))
            curr-=(9-ans[i])
            i+=1
        # print(ans)
        i=len(ans)-2
        while(i>=0):
            if(ans[i]!=9):
                ans[i]+=1
                ans[i+1]-=1
                break
            i-=1
        else:
            return "-1"
        return "".join(map(str,ans))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S,D))
# } Driver Code Ends