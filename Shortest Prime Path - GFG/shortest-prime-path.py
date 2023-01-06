#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
from queue import Queue
class Solution:
    def __init__(self):
        self.prime=[1 for i in range(10001)]
        self.prime[0]=0
        self.prime[1]=0
        i=2
        while(i*i<=10001):
            if(self.prime[i]==1):
                for j in range(i*i,10001,i):
                    self.prime[j]=0
            i+=1
        i=0
        d={}
        for j in range(1000,len(self.prime)):
            if(self.prime[j]==1):
                d[j]=i
                i+=1
        graph=[set() for _ in range(i)]
        for item in d:
            node1=d[item]
            p=1
            t=item
            while(t!=0):
                r=t%10
                tem=item-(r*p)
                for k in range(10):
                    if(k==r or (k==0 and p>1)):
                        continue
                    tem+=(k*p)
                    if(tem in d):
                        node2=d[tem]
                        graph[node1].add(node2)
                        graph[node2].add(node1)
                    tem-=(k*p)
                p*=10
                t//=10
        self.d=d
        self.graph=graph
    def shortestPath(self,Num1,Num2):
        ans=self.find(self.graph,self.d[Num1],self.d[Num2])
        return ans
    def find(self,graph,src,target):
        visited=[False for _ in range(len(graph))]
        obj=Queue()
        obj.put([src,0])
        visited[src]=True
        while(not obj.empty()):
            node,cost=obj.get()
            if(node==target):
                return cost
            for item in graph[node]:
                if(not visited[item]):
                    visited[item]=True
                    obj.put([item,cost+1])
        return -1




#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    ob = Solution()
    for _ in range (t):
        Num1,Num2=map(int,input().split())
        print(ob.shortestPath(Num1,Num2))

# } Driver Code Ends