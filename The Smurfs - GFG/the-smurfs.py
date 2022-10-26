#User function Template for python3

class Solution:
    def minFind(self, n, a):
        r=0
        b=0
        g=0
        for item in a:
            if(item=="R"):
                r+=1
            elif(item=="B"):
                b+=1
            else:
                g+=1
        if(r==n or b==n or g==n):return n
        elif(r%2==b%2 and b%2==g%2):
            return 2
        return 1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        
        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends