class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        stack=[]
        i=0
        while(i<len(s)):
            while(len(s)>i):
                val=s.pop()
                if(len(stack)==0 or stack[-1]<val):
                    stack.append(val)
                else:
                    t=stack.pop()
                    stack.append(val)
                    stack.append(t)
            while(len(stack)!=0):
                s.append(stack.pop())
            i+=1
        s.reverse()



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends