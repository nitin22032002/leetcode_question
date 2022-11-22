#User function Template for python3
from sortedcontainers import SortedList
class Solution:
	def countTriplets(self, nums):
		front=SortedList()
		rare=SortedList()
		front.add(nums[0])
		for i in range(1,len(nums)):
		    rare.add(nums[i])
		i=1
		ans=0
		while(i<len(nums)-1):
		    rare.discard(nums[i])
		    t1=front.bisect_left(nums[i])
		    r1=0
		    if(t1==len(front)):
		        r1=len(front)
		    else:
		        r1=t1
		    t2=rare.bisect_right(nums[i])
		    r2=len(rare)-t2
		    ans+=(r1*r2)
		    front.add(nums[i])
		    i+=1
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends