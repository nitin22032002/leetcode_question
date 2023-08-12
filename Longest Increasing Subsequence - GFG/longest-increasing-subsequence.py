#User function Template for python3
from bisect import bisect_left
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        stack=[]
        for item in a:
            if(len(stack)==0 or stack[-1]<item):
                stack.append(item)
            else:
                j=bisect_left(stack,item)
                stack[j]=item
        return len(stack)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends