#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		d={}
		ans=[]
		for i in range(len(A)):
		    item=A[i]
            if(item not in d):
                d[item]=i
            else:
                d[item]=len(A)
            index=len(A)
            char='#'
            for val in d:
                if(d[val]<index):
                    index=d[val]
                    char=val
            ans.append(char)
        return "".join(ans)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends