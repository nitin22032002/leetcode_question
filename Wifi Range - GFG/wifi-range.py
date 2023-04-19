#User function Template for python3
class Solution:
    def wifiRange(self, N, S, X): 
        count=0
        for i in range(min(X+1,N)):
            if(S[i]=='1'):count+=1
        i=-X
        j=X+1
        k=0
        # print(i,j)
        while(k<N):
            if(S[k]=="0" and count==0):
                # print(k,i,j)
                return False
            if(i>=0 and S[i]=='1'):
                count-=1
            if(j<N and S[j]=='1'):
                count+=1
            i+=1
            j+=1
            k+=1
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends