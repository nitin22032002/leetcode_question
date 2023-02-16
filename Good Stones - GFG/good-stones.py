#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def goodStones(self, n, arr) -> int:
        visited=[False for _ in range(n)]
        isLoop=[-1 for _ in range(n)]
        for i in range(n):
            self.get(arr,i,visited,isLoop)
        ans=0
        for i in range(n):
            if(isLoop[i]==0):
                ans+=1
        return ans
    def get(self,arr,node,visited,isLoop):
        if(isLoop[node]!=-1):
            return isLoop[node]
        elif(visited[node]):
            return 1
        else:
            i=arr[node]+node
            if(i>=len(arr) or i<0):
                isLoop[node]=0
                return 0
            visited[node]=True
            isLoop[node]=self.get(arr,i,visited,isLoop)
            visited[node]=False
            return isLoop[node]

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj=Solution()
        print(obj.goodStones(n, arr))
        
# } Driver Code Ends