#User function Template for python3


#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
def numOfWays(M, N):
    ans=0
    for i in range(N):
        for j in range(M):
            totalMoves=(M*N)
            c=9
            if(i+2>=N):
                c-=2
            else:
                if(j+1>=M):
                    c-=1
                if(j-1<0):
                    c-=1
            if(i-2<0):
                c-=2
            else:
                if(j+1>=M):
                    c-=1
                if(j-1<0):
                    c-=1
            if(j+2>=M):
                c-=2
            else:
                if(i+1>=N):
                    c-=1
                if(i-1<0):
                    c-=1
            if(j-2<0):
                c-=2
            else:
                if(i+1>=N):
                    c-=1
                if(i-1<0):
                    c-=1
            # print((i,j,c,totalMoves))
            ans+=(totalMoves-c)
    return ans%((10**9)+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(numOfWays(m,n))

# } Driver Code Ends