class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        max_ele=-1
        ans=[]
        for i in range(N-1,-1,-1):
            if(max_ele==-1):
                ans.append(A[i])
                max_ele=A[i]
            else:
                if(max_ele<=A[i]):
                    ans.append(A[i])
                    max_ele=A[i]
        ans.reverse()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends