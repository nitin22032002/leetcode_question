#User function Template for python3
class Solution:


	def generateNextPalindrome(self,nums, n ) :
	    i=0
	    j=n-1
	    gret=False
	    while(i<j):
	        if(nums[i]>nums[j]):
	            gret=True
	        elif(nums[i]<nums[j]):
	            gret=False
	        nums[i]=nums[j]=nums[i]
	        i+=1
	        j-=1
	    if(gret):
	        return nums
	    i=n//2
	    while(i<n):
	        if(nums[i]!=9):
	            break
	        i+=1
	    if(i==n):
	        nums.append(0)
	        nums[0]=0
	        j=len(nums)-1
	    j=len(nums)-i-1
	    nums[i]=nums[j]=nums[j]+1
	    j+=1
	    i-=1
	    while(j<=i):
	        nums[j]=nums[i]=0
	        j+=1
	        i-=1
	    return nums


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends