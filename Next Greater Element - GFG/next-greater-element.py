#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        stack=[]
        ans=[-1 for _ in range(len(arr))]
        for i in range(n):
            if(len(stack)==0 or arr[stack[-1]]>=arr[i]):
                stack.append(i)
            else:
                while(len(stack)!=0 and arr[stack[-1]]<arr[i]):
                    ans[stack.pop()]=arr[i]
                stack.append(i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

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
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends