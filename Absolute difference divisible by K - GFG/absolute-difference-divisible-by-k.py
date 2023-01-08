#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        d={}
        ans=0
        for item in arr:
            if(item%k in d):
                ans+=d[item%k]
                d[item%k]+=1
            else:
                d[item%k]=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends