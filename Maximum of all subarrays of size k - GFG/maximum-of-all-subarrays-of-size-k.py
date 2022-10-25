#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        stack=[]
        i=0
        while(i<k):
            if(len(stack)==0 or arr[i]<arr[stack[-1]]):
                stack.append(i)
            else:
                while(len(stack)!=0 and arr[stack[-1]]<=arr[i]):
                    stack.pop()
                stack.append(i)
            i+=1
        j=0
        ind=0
        ans=[]
        while(i<n):
            if(stack[ind]<j):
                ind+=1
            ans.append(arr[stack[ind]])
            if(len(stack)==ind or arr[i]<arr[stack[-1]]):
                stack.append(i)
            else:
                while(len(stack)!=ind and arr[stack[-1]]<=arr[i]):
                    stack.pop()
                stack.append(i)
            i+=1
            j+=1
        if(stack[ind]<j):
                ind+=1
        ans.append(arr[stack[ind]])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends