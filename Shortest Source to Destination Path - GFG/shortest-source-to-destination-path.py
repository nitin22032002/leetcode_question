#User function Template for python3

from queue import Queue
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        obj=Queue()
        visited=[[False for _ in range(M)] for __ in range(N)]
        visited[0][0]=True
        obj.put([0,0,0])
        while(not obj.empty()):
            i,j,cost=obj.get()
            if(i==X and j==Y):return cost
            for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if(i1>=0 and i1<N and j1>=0 and j1<M and not visited[i1][j1] and A[i1][j1]==1):
                    visited[i1][j1]=True
                    obj.put([i1,j1,cost+1])
        return -1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends