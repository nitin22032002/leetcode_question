#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) : 
        d={}
        for item in arr:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        m=max(d)
        ans=0
        while(m>=1):
            ans+=d.get(m)*m
            if(d.get(m-1,0)<=d.get(m)):
                d[m-1]=0
            else:
                d[m-1]-=d.get(m)
            m-=1
        return ans
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends