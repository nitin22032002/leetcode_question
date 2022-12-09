#User function Template for python3

class Solution:

    def buildLowestNumber(self, S,N):
        i=0
        stack=[]
        while(i<len(S)):
            if(len(stack)==0 or stack[-1]<=S[i] or N==0):
                stack.append(S[i])
            else:
                while(len(stack)!=0 and stack[-1]>S[i] and N>0):
                    stack.pop()
                    N-=1
                stack.append(S[i])
            i+=1
        while(N>0 and len(stack)!=0):
            stack.pop()
            N-=1
        i=0
        while(i<len(stack) and stack[i]=='0'):
            i+=1
        stack=stack[i:]
        if(len(stack)==0):
            return "0"
        return "".join(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends