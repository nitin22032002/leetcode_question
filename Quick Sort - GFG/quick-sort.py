#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if(low>=high):
            return
        else:
            index=self.partition(arr,low,high)
            self.quickSort(arr,low,index-1)
            self.quickSort(arr,index+1,high)
    def partition(self,arr,low,high):
        pivot=low
        start=low+1
        end=high
        while(start<=end):
            if(arr[start]>arr[pivot] and arr[end]<=arr[pivot]):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
            elif(arr[start]<=arr[pivot]):start+=1
            else:end-=1
        arr[pivot],arr[end]=arr[end],arr[pivot]
        return end
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends