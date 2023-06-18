class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        i=1
        j=N
        turn=True
        while(i!=j):
            if((j-i+1)<=K):
                if(turn):return j
                return i
            else:
                if(turn):i+=K
                else:j-=K
            turn=not turn
        return i


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends