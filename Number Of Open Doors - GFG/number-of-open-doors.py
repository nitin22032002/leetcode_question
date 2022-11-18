#User function Template for python3

class Solution:
    def noOfOpenDoors(self, n):
        k=pow(n,0.5)
        k=int(k)
        return k
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.noOfOpenDoors(N))
# } Driver Code Ends