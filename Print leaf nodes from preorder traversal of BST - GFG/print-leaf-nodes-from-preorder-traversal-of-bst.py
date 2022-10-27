#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		inorder=sorted(arr)
		d={}
		self.i=0
		for i in range(N):
		    d[inorder[i]]=i
	    ans=[]
	    self.get(d,arr,0,N-1,ans)
	    return ans
	def get(self,inorder,pre,start,end,ans):
	    if(start==end):
	        ans.append(pre[self.i])
	    else:
	        j=inorder[pre[self.i]]
	        if(j!=start):
	            self.i+=1
	            self.get(inorder,pre,start,j-1,ans)
	        if(j!=end):
	            self.i+=1
	            self.get(inorder,pre,j+1,end,ans)
	        return
		



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends