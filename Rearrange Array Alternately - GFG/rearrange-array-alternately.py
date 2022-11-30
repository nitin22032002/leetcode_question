#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        i=0
        j=n-1
        ans=[]
        start=True
        while(j>=i):
            if(start):
                ans.append(arr[j])
                j-=1
            else:
                ans.append(arr[i])
                i+=1
            start=not start
        for i in range(len(arr)):
            arr[i]=ans[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends