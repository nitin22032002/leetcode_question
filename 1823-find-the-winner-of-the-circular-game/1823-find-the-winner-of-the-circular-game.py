class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        visited=[False for _ in range(n)]
        i=0
        curr=0
        while(i!=(n-1)):
            t=1
            while(t<k or visited[curr]):
                if(not visited[curr]):
                    t+=1
                curr+=1
                curr%=n
            visited[curr]=True
            # print(visited)
            i+=1
        for i in range(n):
            if(not visited[i]):
                return i+1
            