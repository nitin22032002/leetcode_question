#User function Template for python3
class Solution:

	def convert(self,arr, n):
		tem=list(enumerate(arr))
		tem.sort(key=lambda x:[x[1],x[0]])
		r=0
		for a,i in tem:
		   arr[a]=r
		   r+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends