#User function Template for python3

class Solution():
    def maximizeMinHeight(self, n, k, w, a):
        start=min(a)
        end=max(a)+k
        while(start<end-1):
            mid=(start+end)//2
            r=self.find(a,mid,w)
            if(r<=k):
                start=mid
            else:
                end=mid-1
        if(self.find(a,end,w)<=k):
            return end
        return start
    def find(self,arr,mid,w):
        start=0
        cost=0
        i=0
        ans=0
        tem=[0 for _ in range(len(arr))]
        while(i<len(arr)):
            if(i-start+1<=w):
                if(arr[i]+cost<mid):
                    tem[i]=(mid-arr[i]-cost)
                    ans+=tem[i]
                    cost+=tem[i]
            else:
                while((i-start+1)>w):
                    cost-=tem[start]
                    start+=1
                if(arr[i]+cost<mid):
                    tem[i]=(mid-arr[i]-cost)
                    cost+=tem[i]
                    ans+=tem[i]
            i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k,w = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(Solution().maximizeMinHeight(n, k, w,arr))

# } Driver Code Ends