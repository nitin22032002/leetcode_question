#User function Template for python3

class Solution():
    def maxSweetness(self, sweetness, n, k):
        start=min(sweetness)
        end=sum(sweetness)
        while(start<end-1):
            mid=(start+end)//2
            r=self.get(sweetness,mid,k)
            if(r):
                end=mid-1
            else:
                start=mid
        if(not self.get(sweetness,end,k)):
            return end
        return start
    def get(self,arr,mid,k):
        count=0
        s=0
        for item in arr:
            if(s+item>=mid):
                s=0
                count+=1
            else:
                s+=item
        # print(count,mid)
        if(count>=(k+1)):
            return False
        return True
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n,k))
# } Driver Code Ends