# User function Template for Python3
from queue import Queue
class Solution:
    def minThrow(self, N, arr):
        d={}
        i=0
        while(i<len(arr)):
            d[arr[i]]=arr[i+1]
            i+=2
        obj=Queue()
        obj.put([0,1])
        visited=[-1 for _ in range(31)]
        visited[1]=0
        while(not obj.empty()):
            cost,node=obj.get()
            if(node==30):
                return cost
            else:
                for i in range(1,min(30-node+1,7)):
                    to=node+i
                    if(to in d):
                        to=d[to]
                    if(visited[to]==-1 or visited[to]>cost+1):
                        visited[to]=cost+1
                        obj.put([cost+1,to])
        return -1
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends