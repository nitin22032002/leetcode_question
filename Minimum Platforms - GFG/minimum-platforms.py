#User function Template for python3
from queue import PriorityQueue
class Solution:    
    def minimumPlatform(self,n,arr,dep):
        obj=PriorityQueue()
        arr=list(enumerate(arr))
        arr.sort(key=lambda x:[x[1],dep[x[0]]])
        ans=0
        for a,b in arr:
            if(obj.empty()):
                obj.put(dep[a])
                ans+=1
            else:
                val=obj.get()
                if(b<=val):
                    ans+=1
                    obj.put(val)
                obj.put(dep[a])
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