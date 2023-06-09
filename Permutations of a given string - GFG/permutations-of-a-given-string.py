#User function Template for python3

class Solution:
    def find_permutation(self, S):
        S=list(S)
        S.sort()
        ans=set()
        self.permut(S,0,ans)
        ans=list(ans)
        ans.sort()
        return ans
    def permut(self,S,i,ans):
        if(i>=len(S)):
            ans.add("".join(S))
        else:
            for j in range(i,len(S)):
                if(j==0 or S[j-1]!=S[j]):
                    if(i!=j and S[i]==S[j]):continue
                    S[i],S[j]=S[j],S[i]
                    (self.permut(S,i+1,ans))
                    S[i],S[j]=S[j],S[i]
                elif(S[j-1]==S[j] and (S[i]!=S[j] or i==j)):
                    (self.permut(S,i+1,ans))
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends