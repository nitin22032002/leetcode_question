#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        s=sum(GeekNum)
        GeekNum.append(s)
        i=0
        while(len(GeekNum)<N):
            GeekNum.append(2*GeekNum[-1]-GeekNum[i])
            i+=1
        return GeekNum[N-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends