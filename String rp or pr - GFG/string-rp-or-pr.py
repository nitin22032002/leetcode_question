#User function Template for python3

class Solution:
    def solve (self, X, Y, S):
        stack=[]
        ans=0
        if(X>Y):
            ans=self.check(S,"pr",X,Y,0)
        else:
            ans=self.check(S,"rp",Y,X,0)
        return ans
    def check(self,S,seq,val1,val2,c):
        if(c==2):return 0
        stack=[]
        ans=0
        for item in S:
            if(len(stack)!=0 and stack[-1]+item==seq):
                ans+=val1
                stack.pop()
            else:
                stack.append(item)
        return ans+self.check(stack,seq[::-1],val2,val1,c+1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends