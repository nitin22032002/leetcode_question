#User function Template for python3
from bisect import bisect_left,bisect_right
class Solution:
    def removeStudents(self, H, N):
        arr=[]
        for i in range(N):
            if(len(arr)==0 or arr[-1]<H[i]):
                arr.append(H[i])
            else:
                j=bisect_left(arr,H[i])
                arr[j]=H[i]
        return N-len(arr)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends