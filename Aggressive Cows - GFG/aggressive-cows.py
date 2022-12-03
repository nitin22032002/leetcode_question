#User function Template for python3
from bisect import bisect_left
class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        # print(stalls)
        start=0
        end=10**9
        while(start<end-1):
            mid=(start+end)//2
            c=self.cost(mid,stalls)
            # print(mid,c,start,end)
            if(c>=k):
                start=mid
            else:
                end=mid-1
        if(self.cost(end,stalls)>=k):
            return end
        return start
    def cost(self,mid,arr):
        i=0
        c=0
        while(i<len(arr)):
            i=bisect_left(arr,arr[i]+mid,i+1,-1)
            c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends