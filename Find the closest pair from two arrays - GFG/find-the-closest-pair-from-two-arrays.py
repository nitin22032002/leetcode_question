#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        j=len(arr)-1
        arr.sort()
        brr.sort()
        diff=1e9
        ans=[-1,-1]
        for i in range(len(brr)):
            d=x-brr[i]
            while(j>=0 and arr[j]>d):j-=1
            if(j>=0):
                if(abs(x-(arr[j]+brr[i]))<diff):
                    diff=abs(x-(arr[j]+brr[i]))
                    ans=[arr[j],brr[i]]
            if(j+1<len(arr)):
                if(abs(x-(arr[j+1]+brr[i]))<diff):
                    diff=abs(x-(arr[j+1]+brr[i]))
                    ans=[arr[j+1],brr[i]]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends