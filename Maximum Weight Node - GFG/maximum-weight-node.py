#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        graph=[0 for _ in range(N)]
        for i in range(len(Edge)):
            item=Edge[i]
            if(item==-1):continue
            graph[item]+=i
        m=-1
        ind=-1
        for i in range(N):
            if(graph[i]>=m):
                m=graph[i]
                ind=i
        return ind


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends