#User function Template for python3

class Solution:
    def minVal(self, a, b):
        c=0
        while(b!=0):
            c+=(b%2)
            b//=2
        ans=0
        for i in range(31,-1,-1):
            bit=(a>>i)&1
            if(bit==1):
                if(c!=0):
                    ans|=(1<<i)
                    c-=1
                else:
                    break
        i=0
        while(i<32 and c!=0):
            bit=(a>>i)&1
            if(bit==0):
                ans|=(1<<i)
                c-=1
            i+=1
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends