#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        start=self.partition(arr)
        for i in range(start+1,n):
            val=arr[i]
            if(abs(val)+start<n):
                arr[start+abs(val)]=-abs(arr[start+abs(val)])
        for i in range(start+1,n):
            if(arr[i]>0):
                return i-start
        return (n-start)
    def partition(self,arr):
        i=0
        target=0
        j=len(arr)-1
        while(i<=j):
            if(arr[i]>target and arr[j]<=target):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            elif(arr[i]<=target):
                i+=1
            else:
                j-=1
        return j


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
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends