#User function Template for python3

class Solution:
    def maxGroupSize(self, arr, N, k):
        d=[0 for _ in range(k)]
        for item in arr:
            d[item%k]+=1
        # print(d)
        ans=[0,0]
        for item in range(k):
            if((k-item==item or item==0) and d[item]!=0):
                ans[0]+=1
                ans[1]+=1
            elif(k-item>item):
                # print(item,d[item],d[k-item])
                ans[0]+=max(d[item],d[(k-item)%k])
                ans[1]+=min(d[item],d[(k-item)%k])
            else:
                break
        return max(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxGroupSize(arr,N,K))
# } Driver Code Ends