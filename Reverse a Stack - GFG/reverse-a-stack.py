#User function Template for python3

from typing import List

class Solution:
    def reverse(self,st): 
        tem=[]
        while(len(st)!=0):
            tem.append(st.pop())
        for item in tem:
            st.append(item)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends