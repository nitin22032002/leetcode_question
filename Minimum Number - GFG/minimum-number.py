#User function Template for python3

class Solution:
    def minimumNumber(self, n, arr):
        prv=arr[0]
        for i in range(1,n):
            val=arr[i]
            val,prv=min(prv,val),max(prv,val)
            while(val!=0):
                d=prv%val
                prv,val=val,d
        return prv


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends