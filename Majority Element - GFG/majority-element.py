#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        element=-1
        count=0
        for item in A:
            if(count==0):
                element=item
                count=1
            elif(element==item):count+=1
            else:count-=1
        c=0
        for item in A:
           if(item==element):c+=1
        if(c>(N/2)):return element
        return -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends