#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        arr=[1,1,2]
        if(n<=2):
            return arr[n]
        mod=int(1e9+7)
        for i in range(n-3,-1,-1):
            val=sum(arr)
            val%=mod
            arr[0],arr[1],arr[2]=arr[1],arr[2],val
        return arr[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends