#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
	    i=j=0
    	while(i<len(arr)):
    	    if(arr[i]==0):
    	        while(j<n and arr[j]==0):j+=1
    	        if(j<n):
    	            arr[i],arr[j]=arr[j],arr[i]
    	    i+=1
    	    j+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends