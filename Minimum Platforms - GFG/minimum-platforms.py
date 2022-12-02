#User function Template for python3
from queue import PriorityQueue
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr=list(zip(arr,dep))
        arr.sort(key=lambda x:x[0])
        obj=PriorityQueue()
        ans=0
        for i in range(n):
            if(obj.qsize()==0):
                obj.put(arr[i][1])
                ans+=1
            else:
                top=obj.get()
                if(top<arr[i][0]):
                    obj.put(arr[i][1])
                else:
                    obj.put(top)
                    obj.put(arr[i][1])
                    ans+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends