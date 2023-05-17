#User function Template for python3

class Solution:
    def isPossible(self, n, m, s):
        up=0
        down=0
        left=0
        right=0
        for item in s:
            if(item=="L"):
                left+=1
                if(right>0):
                    right-=1
            elif(item=="R"):
                right+=1
                if(left>0):
                    left-=1
            elif(item=="U"):
                up+=1
                if(down>0):
                    down-=1
            else:
                down+=1
                if(up>0):
                    up-=1
            if(m-right<=left or n-up<=down):
                # print(left,right,up,down)
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()
        
        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends