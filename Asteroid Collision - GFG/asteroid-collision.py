#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        stack=[]
        for i in range(N):
            if(len(stack)==0 or (stack[-1]>0 and asteroids[i]>0) or (stack[-1]<0 and asteroids[i]<0) or (stack[-1]<0 and asteroids[i]>0)):
                stack.append(asteroids[i])
            else:
                while(len(stack)!=0 and (stack[-1]>0 and asteroids[i]<0)):
                    if(abs(asteroids[i])<abs(stack[-1])):
                        break
                    elif(abs(asteroids[i])==abs(stack[-1])):
                        stack.pop()
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(asteroids[i])
        return stack
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends