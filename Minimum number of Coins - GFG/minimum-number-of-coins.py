#User function Template for python3

class Solution:
    def minPartition(self, N):
        d=[1,2,5,10,20,50,100,200,500,2000]
        ans=[]
        while(N!=0):
            j=self.lower(d,N)
            ans.append(d[j])
            N-=d[j]
        return ans
    def lower(self,arr,target):
        start=0
        end=len(arr)-1
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]==target):
                return mid
            elif(arr[mid]>target):
                end=mid-1
            else:
                start=mid
        if(arr[end]<=target):
            return end
        return start
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends